from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from polymorphic import PolymorphicModel
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class AbstractCategory(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    descrition = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __str__(self):
        return self.name


class AbstractContent(PolymorphicModel):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    published = models.BooleanField(default=True)

    template = None

    def get_template(self):
        if not self.template:
            raise ImproperlyConfigured("Provide a template.")
        return self.template

    def __str__(self):
        return self.title


class ArticleMixin(models.Model):
    class Meta:
        abstract = True

    body = models.TextField()
    publication_time = models.DateTimeField()
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="authors")
    categories = models.ManyToManyField(AbstractCategory)
    tags = TaggableManager(blank=True)


class PageMixin(models.Model):
    class Meta:
        abstract = True

    content = models.TextField()
