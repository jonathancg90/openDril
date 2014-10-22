# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Titulo')),
                ('subject', models.CharField(max_length=50, verbose_name=b'Asunto')),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (2, b'completado'), (3, b'en progreso'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('mandrill_id', models.CharField(max_length=100)),
                ('email_sender', models.EmailField(max_length=45)),
                ('name_sender', models.CharField(max_length=45)),
                ('subject', models.CharField(max_length=45)),
                ('tag', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'rechazado'), (2, b'abierto'), (3, b'invalido'), (5, b'error'), (1, b'enviado'), (4, b'en espera')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(related_name=b'campaign_detail_set', verbose_name=b'Campa\xc3\xb1a', to='mail.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignFilterDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('campaign', models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Campa\xc3\xb1a', to='mail.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Nombre')),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Nombre de la lista')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email para el envio')),
                ('sender', models.CharField(max_length=45, verbose_name=b'Nombre remitente')),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('status', models.SmallIntegerField(default=1, choices=[(0, b'inactivo'), (1, b'activo')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name=b'list_detail_set', verbose_name=b'categoria', blank=True, to='mail.Category', null=True)),
                ('list', models.ForeignKey(related_name=b'list_detail_set', verbose_name=b'Lista', to='mail.List')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.SmallIntegerField(default=1, verbose_name=b'Tipo', choices=[(1, b'Texto'), (2, b'Html')])),
                ('name', models.CharField(max_length=45, verbose_name=b'Nombre')),
                ('content', models.TextField(verbose_name=b'Cuerpo del mensaje')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='list',
            field=models.ForeignKey(related_name=b'category_set', verbose_name=b'Lista', to='mail.List'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaignfilterdetail',
            name='category',
            field=models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Categoria', blank=True, to='mail.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaignfilterdetail',
            name='list',
            field=models.ForeignKey(related_name=b'campaign_filter_detail_set', verbose_name=b'Lista', to='mail.List'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(related_name=b'campaign_set', verbose_name=b'Plantilla', to='mail.Template'),
            preserve_default=True,
        ),
    ]
