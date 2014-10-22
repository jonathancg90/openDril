# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_list_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigndetail',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'rechazado'), (2, b'abierto'), (2, b'abierto'), (1, b'enviado')]),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Nombre de la lista'),
        ),
    ]
