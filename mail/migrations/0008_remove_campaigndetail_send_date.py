# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_auto_20141019_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaigndetail',
            name='send_date',
        ),
    ]
