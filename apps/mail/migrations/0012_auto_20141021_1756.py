# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0011_auto_20141021_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='list',
            field=models.ForeignKey(related_name=b'category_set', default=1, verbose_name=b'Lista', to='mail.List'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='subject',
            field=models.CharField(max_length=50, verbose_name=b'Asunto'),
        ),
        migrations.AlterField(
            model_name='campaignfilterdetail',
            name='category',
            field=models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Categoria', blank=True, to='mail.Category', null=True),
        ),
    ]
