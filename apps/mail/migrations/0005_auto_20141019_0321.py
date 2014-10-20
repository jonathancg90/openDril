# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20141019_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
