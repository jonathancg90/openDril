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

from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.models.CampaignDetail import CampaignDetail
from apps.mail.forms.Campaign import CampaignCreateForm
from apps.mail.models.Campaign import Campaign


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    paginate_by = settings.PAGINATE_SIZE
    template_name = 'campaign/list.html'


class CampaignCreateView(LoginRequiredMixin, CreateView):
    model = Campaign
    form_class = CampaignCreateForm
    success_url = reverse_lazy('campaign_list_view')
    template_name = 'campaign/create.html'


class CampaignUpdateView(LoginRequiredMixin, UpdateView):
    model = Campaign
    success_url = reverse_lazy('campaign_list_view')
    form_class = CampaignCreateForm
    template_name = 'campaign/edit.html'


class CampaignDeleteView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CampaignDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        campaign = Campaign.objects.get(pk=data.get('deleteGroup'))
        campaign.delete()
        return redirect(reverse('campaign_list_view'))


class CampaignDetailListView(LoginRequiredMixin, TemplateView):
    model = CampaignDetail
    template_name = 'campaign/detail.html'
    MESSAGE_WARNING_MESSAGE = 'La informacion se actualizara en algunos minutos'
    CAMPAIGN_WARNING_MESSAGE = 'Campaña invalida'

    def get_queryset(self):
        data = []
        if self.campaign.status == Campaign.STATUS_ACTIVE:
            for list in self.campaign.list.all():
                for detail_list in list.list_detail_set.all():
                    if self.campaign.category == None:
                        data.append({
                            'email': detail_list.email,
                            'state': 'sin enviar',
                            'opens': 0
                        })
                    else:
                        if detail_list.category == self.campaign.category:
                            data.append({
                                'email': detail_list.email,
                                'state': 'sin enviar',
                                'opens': 0
                            })
            return data
        elif self.campaign.status == Campaign.STATUS_SEND:
            mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
            tag = '%s-%s' %(str(self.campaign.id),self.campaign.subject.replace(" ", "-"))
            tags = [tag]
            try:
                results = mandrill_client.messages.search(tags=tags)
                self.campaign.status = Campaign.STATUS_SEND
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
        else:
            messages.warning(self.request, self.CAMPAIGN_WARNING_MESSAGE)
            return data

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailListView, self).get_context_data(**kwargs)
        self.campaign = Campaign.objects.get(pk=self.kwargs.get('pk'))
        context['campaign'] = self.campaign
        context['details'] = self.get_queryset()
        return context