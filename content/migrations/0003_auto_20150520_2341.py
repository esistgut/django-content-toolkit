# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_block_blocktranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, editable=False, related_name='polymorphic_content.categorytranslation_set+'),
        ),
        migrations.AlterField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, editable=False, related_name='polymorphic_content.content_set+'),
        ),
        migrations.AlterField(
            model_name='contenttranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, editable=False, related_name='polymorphic_content.contenttranslation_set+'),
        ),
    ]
