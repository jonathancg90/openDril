# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_auto_20141021_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigndetail',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaigndetail',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'rechazado'), (2, b'abierto'), (3, b'invalido'), (5, b'error'), (1, b'enviado'), (4, b'en espera')]),
        ),
    ]
