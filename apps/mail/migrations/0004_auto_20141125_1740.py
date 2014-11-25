# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20141125_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigndetail',
            name='list_detail',
            field=models.ForeignKey(related_name=b'campaign_detail_set', default=1, verbose_name=b'Detalle de lista', to='mail.ListDetail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listdetail',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')]),
        ),
    ]
