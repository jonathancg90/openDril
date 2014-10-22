# -*- coding: utf-8 -*-
from django.db import models


class Campaign(models.Model):

    STATUS_ACTIVE = 1
    STATUS_SEND = 2
    STATUS_PROGRESS = 3
    STATUS_INACTIVE = 0
    CHOICE_STATUS = (
        (STATUS_INACTIVE,'inactivo'),
        (STATUS_SEND,'completado'), #Termino de neviar todos los mensajes
        (STATUS_PROGRESS,'en progreso'), #Se inicio el envio de mensajes
        (STATUS_ACTIVE,'activo') #Campaña creada peros oin enviar
    )

    name = models.CharField(
        max_length=45,
        verbose_name='Titulo',
    )

    subject = models.CharField(
        max_length=50,
        verbose_name='Asunto',
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

    @property
    def get_lists(self):
        text = ''
        campaign_filter_detail = CampaignFilterDetail.objects.filter(campaign=self)
        if campaign_filter_detail.count() == 0:
            text = 'Ninguna'
        else:
            for filter in campaign_filter_detail:
                text = text + filter.list.name + ' | '
        return text

    class Meta:
        app_label = 'mail'


class CampaignFilterDetail(models.Model):

    campaign = models.ForeignKey(
        'Campaign',
        verbose_name='Campaña',
        related_name='campaign_filter_detail_set',
    )

    list = models.ForeignKey(
        'List',
        verbose_name='Lista',
        related_name='campaign_filter_detail_set',
    )

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        verbose_name='Categoria',
        related_name='campaign_filter_detail_set',
    )

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    class Meta:
        app_label = 'mail'