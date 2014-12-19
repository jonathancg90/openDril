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
from apps.mail.models.Category import Category
from apps.mail.forms.Category import CategoryCreateForm


class CategoryTemplateView(LoginRequiredMixin, ListView):
    model = Category
    paginate_by = settings.PAGINATE_SIZE
    template_name = 'client/category/list.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('category_list_view')
    template_name = 'client/category/create.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    success_url = reverse_lazy('category_list_view')
    form_class = CategoryCreateForm
    template_name = 'client/category/edit.html'


class CategoryDeleteView(LoginRequiredMixin, View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        category = Category.objects.get(pk=data.get('deleteGroup'))
        category.delete()
        return redirect(reverse('category_list_view'))
