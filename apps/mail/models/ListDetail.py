# -*- coding: utf-8 -*-
from django.db import models


class ListDetail(models.Model):

    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0
    CHOICE_STATUS = (
        (STATUS_INACTIVE,'inactivo'),
        (STATUS_ACTIVE,'activo')
    )

    QUALITY_EXCELLENT = 1
    QUALITY_REGULAR = 2
    QUALITY_BAD = 3
    CHOICE_QUALITY = (
        (QUALITY_REGULAR,'Regular'),
        (QUALITY_EXCELLENT,'Bueno'),
        (QUALITY_BAD, 'Malo')
    )

    list = models.ForeignKey(
        'List',
        verbose_name='Lista',
        related_name='list_detail_set',
    )

    name = models.CharField(
        max_length=45,
    )

    category = models.ForeignKey(
        'Category',
        verbose_name='categoria',
        null=True,
        blank=True,
        related_name='list_detail_set',
    )

    email = models.EmailField(
        max_length=45,
    )

    status = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=STATUS_ACTIVE
    )

    quality = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=QUALITY_REGULAR,
        editable=False
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