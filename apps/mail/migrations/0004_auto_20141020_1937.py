# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20141020_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='multiple_email',
            field=models.BooleanField(default=True, verbose_name=b'multiple envio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (2, b'send'), (1, b'activo')]),
        ),
    ]
