# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='list',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'Email para el envio'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='listdetail',
            name='category',
            field=models.ForeignKey(related_name=b'list_detail_set', verbose_name=b'categoria', to='mail.Category', null=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='content',
            field=models.TextField(verbose_name=b'Cuerpo del mensaje'),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Nombre'),
        ),
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.SmallIntegerField(default=1, verbose_name=b'Tipo', choices=[(1, b'Texto'), (2, b'Html')]),
        ),
    ]
