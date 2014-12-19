# -*- coding: utf-8 -*-
import json

from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, RedirectView
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages

from apps.mail.forms.Register import RegisterForm
from apps.mail.models.UserProfile import UserProfile
from apps.mail.models.Business import Business
from apps.mail.views.commons.view import JSONResponseMixin


class HomeTemplateView(TemplateView):
    template_name = 'website/home.html'


class LoginTemplateView(TemplateView):
    template_name = 'website/login.html'


class RegisterTemplateView(FormView):
    MESSAGE_ERROR_PASSWORD = 'Contraseñas no son iguales'
    MESSAGE_ERROR_EMAIL = 'Email ingresado ya se encuentra registrado'
    template_name = 'website/register.html'
    form_class = RegisterForm

    @transaction.commit_on_success
    def form_valid(self, form):
        _form = super(RegisterTemplateView, self).form_valid(form)
        email = form.cleaned_data.get('email')
        company_name = form.cleaned_data.get('company_name')
        phone = form.cleaned_data.get('phone')
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm_password')

        if password != confirm_password:
            messages.error(
                self.request,
                self.MESSAGE_ERROR_PASSWORD
            )
            return super(RegisterTemplateView, self).form_invalid(form)

        if User.objects.filter(email=email).exists():
            messages.error(
                self.request,
                self.MESSAGE_ERROR_EMAIL
            )
            return super(RegisterTemplateView, self).form_invalid(form)
        else:
            user = User()
            user.username = email
            user.email = email
            user.set_password(password)
            user.save()

            user_profile = UserProfile()
            user_profile.role = UserProfile.ROLE_ADMINISTRATOR
            user_profile.user = user
            user_profile.save()

            business = Business()
            business.name = company_name
            business.phone = phone
            business.save()
            business.user.add(user)

        return _form

    def get_success_url(self):
        return reverse('login_template_view')


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
        return reverse('home')