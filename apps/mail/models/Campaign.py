# -*- coding: utf-8 -*-
from django.db import models


class Campaign(models.Model):

    STATUS_ACTIVE = 1
    STATUS_PUBLISH = 2
    STATUS_INACTIVE = 0
    CHOICE_STATUS = (
        (STATUS_INACTIVE,'inactivo'),
        (STATUS_PUBLISH,'publish'),
        (STATUS_ACTIVE,'activo')
    )

    name = models.CharField(
        max_length=45,
    )

    subject = models.CharField(
        max_length=50,
    )

    list = models.ManyToManyField(
        'List',
    )

    template = models.ForeignKey(
        'Template',
        verbose_name='Plantilla',
        related_name='campaign_set',
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