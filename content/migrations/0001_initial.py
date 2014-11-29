# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('slug', models.SlugField(max_length=255)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, related_name='children', null=True, to='content.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('it', 'Italian')], max_length=7)),
                ('name', models.CharField(max_length=255)),
                ('descrition', models.TextField(blank=True)),
                ('master', models.ForeignKey(to='content.Category', related_name='translations')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_content.categorytranslation_set', null=True, to='contenttypes.ContentType', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('content_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='content.Content', primary_key=True)),
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
                ('basearticle_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='content.BaseArticle', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.basearticle',),
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('it', 'Italian')], max_length=7)),
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
                ('contenttranslation_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='content.ContentTranslation', primary_key=True)),
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
                ('content_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='content.Content', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='content.Content', primary_key=True)),
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
            field=models.ForeignKey(related_name='polymorphic_content.contenttranslation_set', null=True, to='contenttypes.ContentType', editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_content.content_set', null=True, to='contenttypes.ContentType', editable=False),
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
            field=taggit.managers.TaggableManager(blank=True, through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ForeignKey(to='content.MediaItem'),
            preserve_default=True,
        ),
    ]
