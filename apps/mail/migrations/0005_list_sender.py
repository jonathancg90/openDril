# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20141020_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='sender',
            field=models.CharField(default=1, max_length=45, verbose_name=b'Nombre remitente'),
            preserve_default=False,
        ),
    ]
