# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_pagetranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
            preserve_default=True,
        ),
    ]
