# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basearticle',
            name='tags',
        ),
        migrations.AddField(
            model_name='basearticletranslation',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', blank=True, verbose_name='Tags', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
    ]
