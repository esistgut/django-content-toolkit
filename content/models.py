from django.db import models
from django.conf import settings

from polymorphic import PolymorphicModel
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager


class AbstractBaseCategory(MPTTModel):
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    descrition = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name


class BaseContent(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AbstractBaseArticle(BaseContent):
    class Meta:
        abstract = True

    content = models.TextField()
    publication_time = models.DateTimeField()
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="authors")
    categories = models.ManyToManyField(AbstractBaseCategory)
    tags = TaggableManager(blank=True)


class AbstractBasePage(BaseContent):
    class Meta:
        abstract = True

    content = models.TextField()
