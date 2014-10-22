# -*- coding: utf-8 -*-
import mandrill
import json

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
from apps.mail.models.Campaign import Campaign, CampaignFilterDetail
from apps.mail.models.List import List
from apps.mail.models.Category import Category
from apps.mail.views.commons.view import JSONResponseMixin


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    paginate_by = settings.PAGINATE_SIZE
    template_name = 'campaign/list.html'

    def get_queryset(self):
        qs = super(CampaignListView, self).get_queryset()
        qs = qs.order_by('-created')
        return qs

    def get_list(self):
        data = []
        lists = List.objects.all()
        for list in lists:
            data.append({
                'list_id': list.id,
                'list_name': list.name,
                'list_categories': self.get_categories_list(list)
            })
        return data

    def get_categories_list(self, list):
        data = []
        categories = Category.objects.filter(list=list)
        for category in categories:
            data.append({
                'category_id': category.id,
                'category_name': category.name
            })
        return data

    def get_context_data(self, **kwargs):
        context = super(CampaignListView, self).get_context_data(**kwargs)
        context['list'] = json.dumps(self.get_list())
        return context


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

    def get_campaign_active(self):
        data = []
        for campaign_detail_filter in self.campaign.campaign_filter_detail_set.all():
            if campaign_detail_filter.category is None:
                list_details = campaign_detail_filter.list.list_detail_set.all()
            else:
                list_details = campaign_detail_filter.list.list_detail_set.filter(category=campaign_detail_filter.category)

            for detail_list in list_details:
                data.append({
                    'email': detail_list.email,
                    'state': 'sin enviar',
                    'opens': 0
                })
        return data

    def get_campaign_send(self):
        data = []
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
                    'state': self.get_status(result.get('state')),
                    'opens': result.get('opens'),
                    'clicks': result.get('clicks')
                })
        except:
            messages.warning(self.request, self.MESSAGE_WARNING_MESSAGE)
        return data

    def get_campaign_progress(self):
        data = []
        for campaign_detail in self.campaign.campaign_detail_set.all():
            data.append({
                'email': campaign_detail.email,
                'state': campaign_detail.get_status_display(),
                'opens': 0,
                'clicks': 0
            })
        return data

    def get_queryset(self):
        data = []
        if self.campaign.status == Campaign.STATUS_ACTIVE:
            data = self.get_campaign_active()
        elif self.campaign.status == Campaign.STATUS_SEND:
            data = self.get_campaign_send()
        elif self.campaign.status == Campaign.STATUS_PROGRESS:
            data = self.get_campaign_progress()
        else:
            messages.warning(self.request, self.CAMPAIGN_WARNING_MESSAGE)
        return data

    def get_status(self, status):
        if status == 'rejected':
            return 'Rechazado'
        if status == 'sent':
            return 'Enviado'
        if status == 'soft-bounced':
            return 'Rebotado'
        if status == 'bounced':
            return 'Rebotado'
        return status

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailListView, self).get_context_data(**kwargs)
        self.campaign = Campaign.objects.get(pk=self.kwargs.get('pk'))
        context['campaign'] = self.campaign
        context['details'] = self.get_queryset()
        return context


class CampaignListDetailView(View, JSONResponseMixin):

    def get(self, request, *args, **kwargs):
        data = []
        campaign = Campaign.objects.get(pk=kwargs.get('campaign'))
        for filter in campaign.campaign_filter_detail_set.all():
            tmp = {
                'detail_id': filter.id,
                'list': filter.list.name,
            }
            if filter.category is not None:
                tmp.update({
                    'category': filter.category.name,
                })
            else:
                tmp.update({
                    'category': 'Todos',
                })

            data.append(tmp)

        return self.render_json_response(data)


class CampaignListDetailCreateView(View, JSONResponseMixin):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CampaignListDetailCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = {}
        data = json.loads(request.body)
        context.update({'status':'warning'})
        try:
            campaign_filter_detail = CampaignFilterDetail.objects.filter(
                campaign_id=data.get('campaign'),
                list_id=data.get('list')
            )

            if not campaign_filter_detail.filter(
                category_id=data.get('category')
            ).exists():
                if campaign_filter_detail.exists() and data.get('category') is None:
                    return self.render_json_response(context)

                campaign_filter = CampaignFilterDetail()
                campaign_filter.campaign_id = data.get('campaign')
                campaign_filter.list_id = data.get('list')
                campaign_filter.category_id = data.get('category')
                campaign_filter.save()
                context.update({'status':'success'})
                context.update({'data': {
                    'detail_id': campaign_filter.id,
                    'list': campaign_filter.list.name,
                    'category': campaign_filter.category.name if campaign_filter.category is not None else 'Todos'
                }})
        except:
            pass
        return self.render_json_response(context)


class CampaignListDetailDeleteView(View, JSONResponseMixin):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CampaignListDetailDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = {}
        data = json.loads(request.body)
        try:
            detail_id = data.get('detail_id')
            CampaignFilterDetail.objects.get(pk=detail_id).delete()
            context.update({'status':'success'})
        except:
            context.update({'status':'warning'})
        return self.render_json_response(context)