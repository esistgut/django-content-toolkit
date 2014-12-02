# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20141202_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttranslation',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
            preserve_default=True,
        ),
    ]
