# -*- coding: utf-8 -*-
from django.db import models


class Template(models.Model):


    name = models.CharField(
        max_length=45,
        verbose_name='Nombre',
    )

    content = models.TextField(
        verbose_name='Cuerpo del mensaje',
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