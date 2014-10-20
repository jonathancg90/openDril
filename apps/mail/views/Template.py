# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import View
from django.views.generic import ListView

from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.models.Template import Template
from apps.mail.forms.Template import TemplateCreateForm


class TemplateView(LoginRequiredMixin, ListView):
    model = Template
    paginate_by = settings.PAGINATE_SIZE
    template_name = 'template/list.html'


class TemplateCreateView(LoginRequiredMixin, CreateView):
    model = Template
    form_class = TemplateCreateForm
    success_url = reverse_lazy('template_list_view')
    template_name = 'template/create.html'


class TemplateUpdateView(LoginRequiredMixin, UpdateView):
    model = Template
    success_url = reverse_lazy('template_list_view')
    form_class = TemplateCreateForm
    template_name = 'template/edit.html'


class TemplateDeleteView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(TemplateDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        template = Template.objects.get(pk=data.get('deleteGroup'))
        template.delete()
        return redirect(reverse('template_list_view'))
