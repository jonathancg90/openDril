# -*- coding: utf-8 -*-
import mandrill

from django.conf import settings
from django.views.generic import TemplateView

from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.models.ListDetail import ListDetail


class DashboardTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'client/dashboard.html'

    def get_information(self):
        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
        result = mandrill_client.users.info()
        data = {
            'hourly_quota': result.get('hourly_quota'),
            'reputation': result.get('reputation'), # 0 to 100, with 75 generally being a "good"
            'backlog': result.get('backlog')
        }
        return data

    def get_context_data(self, **kwargs):
        context = super(DashboardTemplate, self).get_context_data(**kwargs)
        context['information'] = self.get_information()
        return context


class UnSubscribeView(LoginRequiredMixin, TemplateView):
    template_name = 'client/unsubscribe.html'

    def get(self, request, *args, **kwargs):
        list_detail = ListDetail.objects.get(pk=self.kwargs.get('pk'))
        list_detail.status= ListDetail.STATUS_INACTIVE
        list_detail.save()
        return super(UnSubscribeView, self).get(request, *args, **kwargs)