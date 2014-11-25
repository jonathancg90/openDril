# -*- coding: utf-8 -*-
from django.db import models


class CampaignDetail(models.Model):

    STATUS_ERROR = 5
    STATUS_WAIT = 4
    STATUS_INVALID = 3
    STATUS_OPEN = 2
    STATUS_SENT = 1
    STATUS_REJECTED = 0
    CHOICE_STATUS = (
        (STATUS_REJECTED,'rechazado'),
        (STATUS_OPEN,'abierto'),
        (STATUS_INVALID,'invalido'),

        (STATUS_ERROR,'error'),  #Se produjo un error en el envio
        (STATUS_SENT,'enviado'),  #Mensaje enviado por el cron
        (STATUS_WAIT,'en espera') #Mensaje sin enviar espernado al cron
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

    email_sender = models.EmailField(
        max_length=45,
    )

    name_sender = models.CharField(
        max_length=45,
    )

    subject = models.CharField(
        max_length=45,
    )

    tag = models.CharField(
        max_length=50,
    )

    content = models.TextField()

    status = models.SmallIntegerField(
        choices=CHOICE_STATUS,
        default=STATUS_SENT
    )

    list_detail = models.ForeignKey(
        'ListDetail',
        verbose_name='Detalle de lista',
        related_name='campaign_detail_set',
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