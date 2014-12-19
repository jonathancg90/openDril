# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Business(models.Model):

    name = models.CharField(
        max_length=50,
    )

    address = models.CharField(
        max_length=150,
    )

    phone = models.CharField(
        max_length=50,
    )

    logo = models.FileField(
        upload_to="business",
        null=True
    )

    mandrill_api_key = models.CharField(
        max_length=150,
        verbose_name='Mandrill Key',
    )

    user = models.ManyToManyField(
        User
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'mail'