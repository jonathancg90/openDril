# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_auto_20141020_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigndetail',
            name='email_sender',
            field=models.EmailField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaigndetail',
            name='name_sender',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaigndetail',
            name='subject',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaigndetail',
            name='tag',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (2, b'completado'), (3, b'en progreso'), (1, b'activo')]),
        ),
        migrations.AlterField(
            model_name='campaigndetail',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'rechazado'), (2, b'abierto'), (3, b'invalido'), (1, b'enviado'), (4, b'en espera')]),
        ),
    ]
