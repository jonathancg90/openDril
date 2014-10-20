# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_campaigndetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigndetail',
            name='send_date',
            field=models.DateField(default=datetime.date(2014, 10, 18), verbose_name=b'Fecha de envio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (2, b'publish'), (1, b'activo')]),
        ),
    ]
