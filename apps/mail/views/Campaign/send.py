# -*- coding: utf-8 -*-
import mandrill

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