# -*- coding: utf-8 -*-
import mandrill

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.models.CampaignDetail import CampaignDetail
from apps.mail.models.Campaign import Campaign


class SendMessage(LoginRequiredMixin, RedirectView):
    permanent = False
    MESSAGE_SUCCESS = 'Campaña iniciada, sus mensajes estan siendo enviados'
    MESSAGE_ERROR = 'No se pudo enviar su campaña'
    NONE_CAMPAIGN_MESSAGE = 'Su campaña no contiene ningun suscriptor'

    def send_multiple_message_mandrill(self, campaign):
        if len(self.email_list) > 0:
            try:
                mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
                tag = '%s-%s' %(str(campaign.id),campaign.subject.replace(" ", "-"))
                for list in self.email_list:
                    message = {
                                'from_email': list.get('email_sender'),
                                'from_name': list.get('name_sender'),
                                'merge_vars': self.merge_vars,
                                'merge': True,
                                'html':  campaign.template.content,
                                'subject': campaign.subject,
                                'track_opens': True,
                                'track_clicks': True,
                                'to': list.get('details'),
                                'tags': [tag],
                             }
                    results = mandrill_client.messages.send(message=message, async=False)
                campaign.status = Campaign.STATUS_SEND
                campaign.save()
                messages.success(self.request, self.MESSAGE_SUCCESS)
            except mandrill.Error, e:
                messages.warning(self.request, self.MESSAGE_ERROR)
        else:
            messages.warning(self.request, self.NONE_CAMPAIGN_MESSAGE)

    def set_emails(self, campaign):
        self.email_list = []
        self.merge_vars = []
        for list in campaign.list.all():
            details = []
            for detail_list in list.list_detail_set.all():
                if campaign.category is None:
                    details.append(
                        {
                            'email': detail_list.email,
                            'name': detail_list.name,
                            'type': 'to'
                        })

                    self.merge_vars.append(
                        {
                            'rcpt': detail_list.email,
                            'vars': [
                                {
                                    'content': detail_list.name,
                                    'name': 'name'
                                }
                            ]
                        })
                else:
                    if detail_list.category == campaign.category:
                        details.append(
                            {
                                'email': detail_list.email,
                                'name': detail_list.name,
                                'type': 'to'
                            })
                        self.merge_vars.append(
                            {
                                'rcpt': detail_list.email,
                                'vars': [
                                    {
                                        'content': detail_list.name,
                                        'name': 'name'
                                    }
                                ]
                            })
            self.email_list.append({
                'email_sender': list.email,
                'name_sender': list.sender,
                'details': details
            })

    def send_message_mandrill(self):
        pass

    def get_campaign_detail_status(self, status):
        if status == 'sent':
            return CampaignDetail.STATUS_SENT
        if status == 'rejected':
            return CampaignDetail.STATUS_REJECTED
        if status == 'invalid':
            return CampaignDetail.STATUS_INVALID

    def get_redirect_url(self, **kwargs):
        campaign_id = kwargs.get('campaign')
        campaign = Campaign.objects.get(pk=campaign_id)
        if campaign.multiple_email:
            self.set_emails(campaign)
            self.send_multiple_message_mandrill(campaign)
        else:
            self.send_message_mandrill(campaign)
        return reverse('campaign_list_view')