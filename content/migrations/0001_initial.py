# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import taggit.managers
import sortedm2m.fields
from django.conf import settings


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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(to='content.Category', null=True, blank=True, related_name='children')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('language', models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')], max_length=7)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('descrition', models.TextField(blank=True)),
                ('master', models.ForeignKey(to='content.Category', related_name='translations')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, related_name='polymorphic_content.categorytranslation_set', to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('content_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.Content')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('language', models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmal'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('zh-cn', 'Simplified Chinese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese'), ('zh-tw', 'Traditional Chinese')], max_length=7)),
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
                ('contenttranslation_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.ContentTranslation')),
                ('body', models.TextField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags', blank=True, to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.contenttranslation',),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('baseentry_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.BaseEntry')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.baseentry',),
        ),
        migrations.CreateModel(
            name='MediaCollection',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.Content')),
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
                ('content_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='PageTranslation',
            fields=[
                ('contenttranslation_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='content.ContentTranslation')),
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
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='content.MediaItem'),
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
            field=models.ForeignKey(to='content.Content', related_name='translations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, related_name='polymorphic_content.contenttranslation_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, related_name='polymorphic_content.content_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('master', 'language')]),
        ),
        migrations.AddField(
            model_name='baseentry',
            name='authors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='authors'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baseentry',
            name='categories',
            field=models.ManyToManyField(to='content.Category'),
            preserve_default=True,
        ),
    ]
