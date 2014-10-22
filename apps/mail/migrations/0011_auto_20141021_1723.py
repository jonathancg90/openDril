# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0010_campaignfilterdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='category',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='list',
        ),
    ]
