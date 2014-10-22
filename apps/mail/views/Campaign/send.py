# -*- coding: utf-8 -*-
import mandrill

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

from apps.mail.tasks.save_messages import SaveMessagesMandrill
from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.models.CampaignDetail import CampaignDetail
from apps.mail.models.Campaign import Campaign


class SendMessage(LoginRequiredMixin, RedirectView):
    permanent = False
    MESSAGE_SUCCESS = 'Su campaña esta siendo procesada'
    MESSAGE_ERROR = 'No se pudo enviar su campaña'
    NONE_CAMPAIGN_MESSAGE = 'Su campaña no contiene ningun suscriptor'

    def get_redirect_url(self, **kwargs):
        campaign_id = kwargs.get('campaign')
        campaign = Campaign.objects.get(pk=campaign_id)
        campaign.status = Campaign.STATUS_PROGRESS
        campaign.save()
        save_messages_mandrill = SaveMessagesMandrill()
        params = {
            'campaign': campaign,
        }
        save_messages_mandrill.delay(**params)
        messages.success(self.request, self.MESSAGE_SUCCESS)
        return reverse('campaign_list_view')


class SendTestMessage(LoginRequiredMixin, RedirectView):
    MESSAGE_SUCCESS = 'Mensaje de prueba enviado'
    MESSAGE_ERROR = 'No se pudo enviar el correo de prueba'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SendTestMessage, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        campaign_id = kwargs.get('campaign')
        email_send = self.request.POST.get('email')
        name_send = self.request.POST.get('name')

        campaign = Campaign.objects.get(pk=campaign_id)
        try:
            mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
            message = {
                'from_email': 'sistemas3@nexonet.net',
                'from_name': 'tester',
                'merge_vars': [{
                                   'rcpt': email_send,
                                   'vars': [
                                       {
                                           'content': name_send,
                                           'name': 'name'
                                       }
                                   ]
                               }],
                'merge': True,
                'html':  campaign.template.content,
                'subject': campaign.subject,
                'track_opens': True,
                'track_clicks': True,
                'to':[{
                          'email': email_send,
                          'name': name_send,
                          'type': 'to'
                      }],
                'tags': ['test-message'],
                }
            result = mandrill_client.messages.send(message=message, async=False)

            messages.success(self.request, self.MESSAGE_SUCCESS)
        except:
            messages.warning(self.request, self.MESSAGE_ERROR)
        return reverse('campaign_list_view')