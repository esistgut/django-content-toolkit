# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_mediacollection_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediacollection',
            name='items',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='content.MediaItem'),
            preserve_default=True,
        ),
    ]
