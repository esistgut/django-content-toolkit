import os

from django.db import models
from django.conf import settings
from django.conf import global_settings
from django.utils import translation
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist

import reversion
from polymorphic import PolymorphicModel
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from sortedm2m.fields import SortedManyToManyField


class TranslatedModel(models.Model):
    class Meta:
        abstract = True

    @property
    def translation(self):
        language_code = translation.get_language()
        try:
            return self.translations.get(language=language_code)
        except ObjectDoesNotExist:
            return self.translations.get(language=settings.LANGUAGE_CODE)


class AbstractTranslation(PolymorphicModel):
    # https://code.djangoproject.com/ticket/16732
    class Meta:
        abstract = True
        #unique_together = (('master', 'language'),)

    @property
    def master(self):
        raise ImproperlyConfigured

    language = models.CharField(max_length=7, choices=global_settings.LANGUAGES)


class Category(TranslatedModel, MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __str__(self):
        return self.translation.title


class CategoryTranslation(AbstractTranslation):
    class Meta:
        unique_together = (('master', 'language'),)
    master = models.ForeignKey('Category', related_name='translations')

    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    descrition = models.TextField(blank=True)


class Content(TranslatedModel, PolymorphicModel):
    published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('content-detail', args=[self.translation.slug, ])

    def __str__(self):
        return self.translation.title
        

class ContentTranslation(AbstractTranslation):
    class Meta:
        unique_together = (('master', 'language'),)

    master = models.ForeignKey('Content', related_name='translations')

    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    

class BaseEntry(Content):
    publication_time = models.DateTimeField()
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="authors")
    categories = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return reverse('entry-detail', args=[
            self.publication_time.year,
            self.publication_time.strftime('%m'),
            self.publication_time.strftime('%d'),
            self.translation.slug, ])


class BaseEntryTranslation(ContentTranslation):
    body = models.TextField()
    tags = TaggableManager(blank=True)


class Entry(BaseEntry):
    image = models.ForeignKey('MediaItem')


class Page(Content):
    pass


class PageTranslation(ContentTranslation):
    body = models.TextField()


class Block(Content):
    pass


class BlockTranslation(ContentTranslation):
    body = models.TextField()
    

class MediaItem(Content):
    file = models.FileField()

    def __str__(self):
        return self.file.url


class MediaCollection(Content):
    items = SortedManyToManyField(MediaItem)


@receiver(models.signals.post_delete, sender=MediaItem)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=MediaItem)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = MediaItem.objects.get(pk=instance.pk).file
    except MediaItem.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


reversion.register(Category, follow=('translations', ))
reversion.register(CategoryTranslation)
reversion.register(Content, follow=('translations', ))
reversion.register(ContentTranslation)
reversion.register(Page)
reversion.register(PageTranslation)
reversion.register(BaseEntry, follow=('categories', 'authors', ))
reversion.register(BaseEntryTranslation)
