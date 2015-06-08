# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150520_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, related_name='polymorphic_content.categorytranslation_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, related_name='polymorphic_content.content_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contenttranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, related_name='polymorphic_content.contenttranslation_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]
