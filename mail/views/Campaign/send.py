import mandrill
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from mail.models.CampaignDetail import CampaignDetail
from django.views.generic import ListView
from django.views.generic import RedirectView

from mail.models.Campaign import Campaign


class SendMessage(RedirectView):
    permanent = False

    def send_message_mandrill(self, campaign):
        if len(self.emails) > 0:
            mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
            message = {
                        'from_email': 'sistemas3@nexonet.net',
                        'from_name': 'Nexonet',
                        'html':  campaign.template.content,
                        'subject': campaign.subject,
                        'track_opens': True,
                        'to': self.emails,
                        'tags': [campaign.subject.replace(" ", "-")],
                     }
            results = mandrill_client.messages.send(message=message, async=False)
            campaign.status = Campaign.STATUS_PUBLISH
            campaign.save()
            # for result in results:
            #     campaign_detail = CampaignDetail()
            #     campaign_detail.campaign = campaign
            #     campaign_detail.email = result.get('email')
            #     campaign_detail.mandrill_id = result.get('_id')
            #     if result.get('status') == 'sent':
            #         campaign_detail.status = CampaignDetail.STATUS_SENT
            #     if result.get('status') == 'rejected':
            #         return CampaignDetail.STATUS_REJECTED
            #     if result.get('status') == 'invalid':
            #         return CampaignDetail.STATUS_INVALID
            #     campaign_detail.save()
            # else:
            #     return None

    def set_emails(self, campaign):
        self.emails = []
        for list in campaign.list.all():
            for detail_list in list.list_detail_set.all():
                self.emails.append(
                    {
                        'email': detail_list.email,
                        'name': detail_list.name,
                        'type': 'to'
                    })

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
        self.set_emails(campaign)
        self.send_message_mandrill(campaign)
        return reverse('campaign_list_view')