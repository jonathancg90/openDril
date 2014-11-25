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
from apps.mail.models.List import List
from apps.mail.forms.List import ListCreateForm


class ListTemplateView(LoginRequiredMixin, ListView):
    model = List
    paginate_by = settings.PAGINATE_SIZE
    template_name = 'list/list.html'

    def get_queryset(self):
        qs = super(ListTemplateView, self).get_queryset()
        qs= qs.filter(status=List.STATUS_ACTIVE)
        return qs


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    form_class = ListCreateForm
    success_url = reverse_lazy('list_view')
    template_name = 'list/create.html'


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    success_url = reverse_lazy('list_view')
    form_class = ListCreateForm
    template_name = 'list/edit.html'


class ListDeleteView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ListDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        list = List.objects.get(pk=data.get('deleteGroup'))
        list.delete()
        return redirect(reverse('list_view'))
