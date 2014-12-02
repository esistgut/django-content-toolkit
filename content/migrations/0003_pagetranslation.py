# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20141201_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(to='content.ContentTranslation', primary_key=True, auto_created=True, parent_link=True, serialize=False)),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.contenttranslation',),
        ),
    ]
