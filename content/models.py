from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from polymorphic import PolymorphicModel
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class Category(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    descrition = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __str__(self):
        return self.name


class Content(PolymorphicModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Article(Content):
    body = models.TextField()
    publication_time = models.DateTimeField()
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="authors")
    categories = models.ManyToManyField(Category)
    tags = TaggableManager(blank=True)


class Page(Content):
    body = models.TextField()


class MediaItem(Content):
    file = models.FileField()
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.file.url


class MediaColletion(Content):
    items = models.ManyToManyField(MediaItem)
