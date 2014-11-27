# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('slug', models.SlugField(max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('language', models.CharField(choices=[('en', 'English'), ('it', 'Italian')], max_length=7)),
                ('name', models.CharField(max_length=255)),
                ('descrition', models.TextField(blank=True)),
                ('master', models.ForeignKey(to='content.Category', related_name='translations')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, to='contenttypes.ContentType', null=True, related_name='polymorphic_content.categorytranslation_set')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('slug', models.SlugField(max_length=255)),
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
                ('content_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='content.Content', auto_created=True, serialize=False)),
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
                ('basearticle_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='content.BaseArticle', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.basearticle',),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('language', models.CharField(choices=[('en', 'English'), ('it', 'Italian')], max_length=7)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseArticleTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='content.ContentTranslation', auto_created=True, serialize=False)),
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
                ('content_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='content.Content', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='content.Content', auto_created=True, serialize=False)),
                ('file', models.FileField(upload_to='')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', blank=True, through='taggit.TaggedItem', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='content.Content', auto_created=True, serialize=False)),
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
            field=models.ForeignKey(editable=False, to='contenttypes.ContentType', null=True, related_name='polymorphic_content.contenttranslation_set'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, to='contenttypes.ContentType', null=True, related_name='polymorphic_content.content_set'),
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
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', blank=True, through='taggit.TaggedItem', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(to='content.MediaItem'),
            preserve_default=True,
        ),
    ]
