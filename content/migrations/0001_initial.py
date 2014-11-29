# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields
import taggit.managers


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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, to='content.Category', related_name='children')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=7, choices=[('en', 'English'), ('it', 'Italian')])),
                ('slug', models.SlugField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('descrition', models.TextField(blank=True)),
                ('master', models.ForeignKey(to='content.Category', related_name='translations')),
                ('polymorphic_ctype', models.ForeignKey(null=True, editable=False, to='contenttypes.ContentType', related_name='polymorphic_content.categorytranslation_set')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseArticle',
            fields=[
                ('content_ptr', models.OneToOneField(to='content.Content', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('publication_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('basearticle_ptr', models.OneToOneField(to='content.BaseArticle', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.basearticle',),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=7, choices=[('en', 'English'), ('it', 'Italian')])),
                ('slug', models.SlugField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseArticleTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(to='content.ContentTranslation', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('content.contenttranslation',),
        ),
        migrations.CreateModel(
            name='MediaCollection',
            fields=[
                ('content_ptr', models.OneToOneField(to='content.Content', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('content_ptr', models.OneToOneField(to='content.Content', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(to='content.Content', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='items',
            field=models.ManyToManyField(to='content.MediaItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='master',
            field=models.ForeignKey(to='content.Content', related_name='translations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(null=True, editable=False, to='contenttypes.ContentType', related_name='polymorphic_content.contenttranslation_set'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(null=True, editable=False, to='contenttypes.ContentType', related_name='polymorphic_content.content_set'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='basearticle',
            name='authors',
            field=models.ManyToManyField(verbose_name='authors', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basearticle',
            name='categories',
            field=models.ManyToManyField(to='content.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='basearticle',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(to='content.MediaItem'),
            preserve_default=True,
        ),
    ]
