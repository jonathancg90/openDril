# -*- coding: utf-8 -*-
import json

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, RedirectView
from django.contrib import auth

from apps.mail.views.commons.view import LoginRequiredMixin
from apps.mail.views.commons.view import JSONResponseMixin


class dashboardTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class HomeTemplate(TemplateView):
    template_name = 'home.html'


class LoginUserView(View, JSONResponseMixin):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LoginUserView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = {}
        context.update({'status':'warning'})
        data = json.loads(request.body)

        user = data.get('username')
        password = data.get('password')

        user = auth.authenticate(
            username=user,
            password=password
        )
        if user is not None and user.is_active:
            auth.login(self.request, user)
            context.update({'status': 200})
            context.update({'message': 'Bienvenido'})
            context.update({'home_url':  reverse('dashboard_view') })
        else:
            context.update({'message': 'Login invalido'})
        return self.render_json_response(context)


class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse('home_view')