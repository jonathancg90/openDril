# -*- coding: utf-8 -*-
from django.db import models


class Template(models.Model):

    TYPE_TEXT = 1
    TYPE_HTML = 2
    CHOICE_TYPES = (
        (TYPE_TEXT,'Texto'),
        (TYPE_HTML,'Html'),
    )

    type = models.SmallIntegerField(
        choices=CHOICE_TYPES,
        default=TYPE_TEXT,
        verbose_name='Tipo',
    )

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