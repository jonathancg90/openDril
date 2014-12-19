# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper


class RegisterForm(forms.Form):

    company_name = forms.CharField(
        label='Nombre de su compañia',
        max_length=50,
        required=True
    )

    email = forms.EmailField(
        label='Correo',
        required=True
    )

    phone = forms.CharField(
        label='Telefono',
        required=False
    )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        label='Confirma tu contraseña',
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        super(RegisterForm, self).__init__(*args, **kwargs)

