# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_template_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='subject',
        ),
        migrations.AddField(
            model_name='campaign',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
