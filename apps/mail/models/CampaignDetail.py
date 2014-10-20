# -*- coding: utf-8 -*-
from django.db import models


class CampaignDetail(models.Model):

    STATUS_INVALID = 3
    STATUS_OPEN = 2
    STATUS_SENT = 1
    STATUS_REJECTED = 0
    CHOICE_STATUS = (
        (STATUS_REJECTED,'rechazado'),
        (STATUS_OPEN,'abierto'),
        (STATUS_SENT,'enviado')
    )

    campaign = models.ForeignKey(
        'Campaign',
        verbose_name='Campaña',
        related_name='campaign_detail_set',
    )

    name = models.CharField(
        max_length=45,
    )

    email = models.EmailField(
        max_length=45,
    )

    mandrill_id = models.CharField(
        max_length=100,
    )

    status = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=STATUS_SENT
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