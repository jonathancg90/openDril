# -*- coding: utf-8 -*-
import mandrill
from datetime import timedelta
from django.conf import settings

from celery.task import Task
from celery.task import PeriodicTask

from apps.mail.models.Campaign import Campaign
from apps.mail.models.CampaignDetail import  CampaignDetail


class SendMessagesMandrill(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(self, *args, **kwargs):
        campaigns = Campaign.objects.filter(status=Campaign.STATUS_PROGRESS)
        for campaign in campaigns:
            self.send_message_mandrill(campaign)
        # if campaign.multiple_email:
        #     self.set_emails(campaign)
        #     self.send_multiple_message_mandrill(campaign)
        # else:
        #     self.send_message_mandrill(campaign)

    # def send_multiple_message_mandrill(self, campaign):
    #     if len(self.email_list) > 0:
    #         try:
    #             mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
    #             info = mandrill_client.users.info()
    #             tag = '%s-%s' %(str(campaign.id),campaign.subject.replace(" ", "-"))
    #             for list in self.email_list:
    #                 message = {
    #                     'from_email': list.get('email_sender'),
    #                     'from_name': list.get('name_sender'),
    #                     'merge_vars': self.merge_vars,
    #                     'merge': True,
    #                     'html':  campaign.template.content,
    #                     'subject': campaign.subject,
    #                     'track_opens': True,
    #                     'track_clicks': True,
    #                     'to': list.get('details'),
    #                     'tags': [tag],
    #                     }
    #                 results = mandrill_client.messages.send(message=message, async=False)
    #             campaign.status = Campaign.STATUS_SEND
    #             campaign.save()
    #         except mandrill.Error, e:
    #             pass
    #             # TODO: mensaje error
    #     else:
    #         pass
    #         # TODO: campign detils none

    # def set_emails(self, campaign):
    #     self.email_list = []
    #     self.merge_vars = []
    #     for list in campaign.list.all():
    #         details = []
    #         for detail_list in list.list_detail_set.all():
    #             if campaign.category is None:
    #                 details.append(
    #                     {
    #                         'email': detail_list.email,
    #                         'name': detail_list.name,
    #                         'type': 'to'
    #                     })
    #
    #                 self.merge_vars.append(
    #                     {
    #                         'rcpt': detail_list.email,
    #                         'vars': [
    #                             {
    #                                 'content': detail_list.name,
    #                                 'name': 'name'
    #                             }
    #                         ]
    #                     })
    #             else:
    #                 if detail_list.category == campaign.category:
    #                     details.append(
    #                         {
    #                             'email': detail_list.email,
    #                             'name': detail_list.name,
    #                             'type': 'to'
    #                         })
    #                     self.merge_vars.append(
    #                         {
    #                             'rcpt': detail_list.email,
    #                             'vars': [
    #                                 {
    #                                     'content': detail_list.name,
    #                                     'name': 'name'
    #                                 }
    #                             ]
    #                         })
    #         self.email_list.append({
    #             'email_sender': list.email,
    #             'name_sender': list.sender,
    #             'details': details
    #         })

    def send_message_mandrill(self, campaign):
        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
        campaign_details = campaign.campaign_detail_set.filter(status=CampaignDetail.STATUS_WAIT)
        if campaign_details.count() == 0:
            campaign.status = Campaign.STATUS_SEND
            campaign.save()
            return
        for campaign_detail in campaign_details:
            # info = mandrill_client.users.info()
            try:
                message = {
                    'from_email': campaign_detail.email_sender,
                    'from_name': campaign_detail.name_sender,
                    'merge_vars': [{
                                       'rcpt': campaign_detail.email,
                                       'vars': [
                                           {
                                               'content': campaign_detail.name,
                                               'name': 'name'
                                           }
                                       ]
                                   }],
                    'merge': True,
                    'html':  campaign_detail.content,
                    'subject': campaign.subject,
                    'track_opens': True,
                    'track_clicks': True,
                    'to':[{
                              'email': campaign_detail.email,
                              'name': campaign_detail.name,
                              'type': 'to'
                          }],
                    'tags': [campaign_detail.tag],
                    }
                result = mandrill_client.messages.send(message=message, async=False)
                campaign_detail.mandrill_id = result[0].get('_id')
                campaign_detail.status = CampaignDetail.STATUS_SENT
                campaign_detail.save()

            except mandrill.Error, e:
                campaign_detail.status = CampaignDetail.STATUS_ERROR
                campaign_detail.save()
