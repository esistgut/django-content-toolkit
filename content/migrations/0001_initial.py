# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, to='content.Category', null=True, related_name='children')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('it', 'Italian')], max_length=7)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('descrition', models.TextField(blank=True)),
                ('master', models.ForeignKey(related_name='translations', to='content.Category')),
                ('polymorphic_ctype', models.ForeignKey(to='contenttypes.ContentType', null=True, related_name='polymorphic_content.categorytranslation_set', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseEntry',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='content.Content', auto_created=True, serialize=False)),
                ('publication_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('it', 'Italian')], max_length=7)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseEntryTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='content.ContentTranslation', auto_created=True, serialize=False)),
                ('body', models.TextField()),
                ('tags', taggit.managers.TaggableManager(blank=True, verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.contenttranslation',),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('baseentry_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='content.BaseEntry', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.baseentry',),
        ),
        migrations.CreateModel(
            name='MediaCollection',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='content.Content', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='content.Content', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='content.ContentTranslation', auto_created=True, serialize=False)),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.contenttranslation',),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='items',
            field=models.ManyToManyField(to='content.MediaItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ForeignKey(to='content.MediaItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', to='content.Content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, related_name='polymorphic_content.contenttranslation_set', editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True, related_name='polymorphic_content.content_set', editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='baseentry',
            name='authors',
            field=models.ManyToManyField(verbose_name='authors', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baseentry',
            name='categories',
            field=models.ManyToManyField(to='content.Category'),
            preserve_default=True,
        ),
    ]
