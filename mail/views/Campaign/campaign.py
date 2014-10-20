# -*- coding: utf-8 -*-
import mandrill

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import View

from mail.models.CampaignDetail import CampaignDetail
from mail.forms.Campaign import CampaignCreateForm
from mail.models.Campaign import Campaign


class CampaignListView(ListView):
    model = Campaign
    template_name = 'campaign/list.html'


class CampaignCreateView(CreateView):
    model = Campaign
    form_class = CampaignCreateForm
    success_url = reverse_lazy('campaign_list_view')
    template_name = 'campaign/create.html'


class CampaignUpdateView(UpdateView):
    model = Campaign
    success_url = reverse_lazy('campaign_list_view')
    form_class = CampaignCreateForm
    template_name = 'campaign/edit.html'


class CampaignDeleteView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CampaignDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        campaign = Campaign.objects.get(pk=data.get('deleteGroup'))
        campaign.delete()
        return redirect(reverse('campaign_list_view'))


class CampaignDetailListView(TemplateView):
    model = CampaignDetail
    template_name = 'campaign/detail.html'
    MESSAGE_WARNING_MESSAGE = 'Envio de mensajes en proceso ...'

    def get_queryset(self):
        data = []
        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
        tags = [self.campaign.subject.replace(" ", "-")]
        try:
            results = mandrill_client.messages.search(tags=tags)
            self.campaign.status = Campaign.STATUS_PUBLISH
            self.campaign.save()
            if len(results) == 0:
                messages.warning(self.request, self.MESSAGE_WARNING_MESSAGE)
                return data

            for result in results:
                data.append({
                    'email': result.get('email'),
                    'state': result.get('state'),
                    'opens': result.get('opens')
                })
        except:
            messages.warning(self.request, self.MESSAGE_WARNING_MESSAGE)
        return data

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailListView, self).get_context_data(**kwargs)
        self.campaign = Campaign.objects.get(pk=self.kwargs.get('pk'))
        context['campaign'] = self.campaign
        context['details'] = self.get_queryset()
        return context