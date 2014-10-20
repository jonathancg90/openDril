# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20141018_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.SmallIntegerField(default=1, choices=[(1, b'Texto'), (2, b'Html')])),
                ('name', models.TextField(max_length=45)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='campaign',
            name='template',
            field=models.ForeignKey(related_name=b'campaign_set', default=1, verbose_name=b'Plantilla', to='apps.mail.Template'),
            preserve_default=False,
        ),
    ]
