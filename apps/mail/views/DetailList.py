# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import View

from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.forms.ListDetail import ListDetailCreateForm
from apps.mail.models.ListDetail import ListDetail
from apps.mail.models.Category import Category
from apps.mail.models.List import List


class ListDetailView(LoginRequiredMixin, ListView):
    model = ListDetail
    paginate_by = settings.PAGINATE_SIZE
    template_name = 'list_detail/list.html'

    def get_queryset(self):
        qs = super(ListDetailView, self).get_queryset()
        qs = qs.filter(list_id=self.kwargs.get('pk'))
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListDetailView, self).get_context_data(**kwargs)
        context['list'] = List.objects.get(pk=self.kwargs.get('pk'))
        return context


class ListDetailCreateView(LoginRequiredMixin, CreateView):
    model = ListDetail
    form_class = ListDetailCreateForm
    template_name = 'list_detail/create.html'

    def get_success_url(self):
        return reverse('list_detail_view', kwargs={'pk': self.kwargs.get('list')})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.list = List.objects.get(pk=self.kwargs.get('list'))
        self.object.save()
        return super(ListDetailCreateView, self).form_valid(form)

    def get_form(self, form_class):
        list = List.objects.get(pk=self.kwargs.get('list'))
        form = super(ListDetailCreateView, self).get_form(form_class)
        if self.request.POST.get('category') is None:
            form.set_category(list)
        return form

    def get_context_data(self, **kwargs):
        context = super(ListDetailCreateView, self).get_context_data(**kwargs)
        context['list'] = List.objects.get(pk=self.kwargs.get('list'))
        return context


class ListDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = ListDetail
    form_class = ListDetailCreateForm
    template_name = 'list_detail/edit.html'

    def get_form(self, form_class):
        form = super(ListDetailUpdateView, self).get_form(form_class)
        if self.request.POST.get('category') is None:
            if self.object.category is not None:
                form.set_category_update(self.object.list, self.object.category)
            else:
                form.set_category(self.object.list)
        return form

    def get_success_url(self):
        return reverse('list_detail_view', kwargs={'pk':  self.object.list.id})


class ListDetailDeleteView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ListDetailDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        list_detail = ListDetail.objects.get(pk=data.get('deleteGroup'))
        list_id = list_detail.list.id
        list_detail.delete()
        return redirect(reverse('list_detail_view', kwargs={'pk': list_id}))
