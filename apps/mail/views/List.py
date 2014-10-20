# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import View
from django.views.generic import ListView

from apps.mail.models.List import List
from apps.mail.forms.List import ListCreateForm


class ListTemplateView(ListView):
    model = List
    template_name = 'list/list.html'


class ListCreateView(CreateView):
    model = List
    form_class = ListCreateForm
    success_url = reverse_lazy('list_view')
    template_name = 'list/create.html'


class ListUpdateView(UpdateView):
    model = List
    success_url = reverse_lazy('list_view')
    form_class = ListCreateForm
    template_name = 'list/edit.html'


class ListDeleteView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ListDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        list = List.objects.get(pk=data.get('deleteGroup'))
        list.delete()
        return redirect(reverse('list_view'))
