# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_auto_20141019_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
