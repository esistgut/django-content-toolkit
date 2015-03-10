# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='content.Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='BlockTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, serialize=False, to='content.ContentTranslation')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.contenttranslation',),
        ),
    ]
