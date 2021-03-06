# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):

    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0
    CHOICE_STATUS = (
        (STATUS_INACTIVE,'inactivo'),
        (STATUS_ACTIVE,'activo')
    )

    business = models.ForeignKey(
        'Business',
        related_name='category_set',
    )

    name = models.CharField(
        max_length=45,
        verbose_name='Nombre',
    )

    list = models.ForeignKey(
        'List',
        verbose_name='Lista',
        related_name='category_set',
    )

    status = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=STATUS_ACTIVE
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