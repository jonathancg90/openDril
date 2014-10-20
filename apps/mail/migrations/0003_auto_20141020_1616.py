# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20141020_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='category',
            field=models.ForeignKey(related_name=b'campaign_set', verbose_name=b'Categoria', blank=True, to='mail.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listdetail',
            name='category',
            field=models.ForeignKey(related_name=b'list_detail_set', verbose_name=b'categoria', blank=True, to='mail.Category', null=True),
        ),
    ]
