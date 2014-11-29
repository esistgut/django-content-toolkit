# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, related_name='children', to='content.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('language', models.CharField(max_length=7, choices=[('en', 'English'), ('it', 'Italian')])),
                ('name', models.CharField(max_length=255)),
                ('descrition', models.TextField(blank=True)),
                ('master', models.ForeignKey(related_name='translations', to='content.Category')),
                ('polymorphic_ctype', models.ForeignKey(null=True, editable=False, related_name='polymorphic_content.categorytranslation_set', to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('content_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.Content')),
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
                ('basearticle_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.BaseArticle')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.basearticle',),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('contenttranslation_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='content.ContentTranslation')),
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
            field=models.ForeignKey(related_name='translations', to='content.Content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(null=True, editable=False, related_name='polymorphic_content.contenttranslation_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(null=True, editable=False, related_name='polymorphic_content.content_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='basearticle',
            name='authors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='authors'),
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
            field=taggit.managers.TaggableManager(blank=True, verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(to='content.MediaItem'),
            preserve_default=True,
        ),
    ]
