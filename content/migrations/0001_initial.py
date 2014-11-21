# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('descrition', models.TextField()),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(null=True, to='content.Category', blank=True, related_name='children')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.Content')),
                ('body', models.TextField()),
                ('publication_time', models.DateTimeField()),
                ('authors', models.ManyToManyField(verbose_name='authors', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='content.Category')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', blank=True, help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaColletion',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.Content')),
                ('file', models.FileField(upload_to='')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', blank=True, help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.Content')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.AddField(
            model_name='mediacolletion',
            name='items',
            field=models.ManyToManyField(to='content.MediaItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, to='contenttypes.ContentType', related_name='polymorphic_content.content_set'),
            preserve_default=True,
        ),
    ]
