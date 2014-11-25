# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_remove_template_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='listdetail',
            name='quality',
            field=models.SmallIntegerField(default=2, editable=False, choices=[(0, b'inactivo'), (1, b'activo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listdetail',
            name='status',
            field=models.SmallIntegerField(default=2, choices=[(0, b'inactivo'), (1, b'activo')]),
        ),
    ]
