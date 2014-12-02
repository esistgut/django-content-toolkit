from django import forms
from django.conf import settings
from django.db import models
from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static

from reversion import VersionAdmin
from sorl.thumbnail import get_thumbnail

from .forms import AtLeastOneRequiredInlineFormSet
from .models import (
    ContentTranslation, BaseArticleTranslation, Article, Page, PageTranslation,
    Category, CategoryTranslation, MediaItem, MediaCollection,
)


class CKModelAdminMixin(object):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = [
            static('content/ckeditor/ckeditor.js'),
            static('content/ckeditor_setup.js'),
        ]

        css = {
            'all': (static('content/ckeditor_style_override.css'),)
        }


class CKMediaItemAdmin(admin.ModelAdmin, CKModelAdminMixin):
    def thumbnail(self, obj):
        if self.list_display_links is not None:
            return u'<img src="%s" />' % get_thumbnail(obj.file, '125x125', crop='center').url
        else:
            return u'<a href="%s" class="cklink"><img src="%s" /></a>' % (obj.file.url, get_thumbnail(obj.file, '125x125', crop='center').url)

    thumbnail.short_description = 'Thumb'
    thumbnail.allow_tags = True

    def changelist_view(self, request, extra_context=None, **kwargs):
        request.GET._mutable = True

        if 'CKEditor' in request.GET:
            request.GET.pop('CKEditor')
            request.GET.pop('langCode')
            asd = request.GET.pop('CKEditorFuncNum')
            request.session['CKEditorFuncNum'] = asd[0]
            request.session['asd'] = "klplkdglaskglaskdgl"
            request.session.save()
            self.list_display_links = None
        else:
            self.list_display_links = self._list_display_links_copy

        request.GET_mutable = False

        return super().changelist_view(request, extra_context=extra_context)

    def __init__(self, *args, **kwargs):
        self._list_display_links_copy = self.list_display_links
        super().__init__(*args, **kwargs)


class TranslationInline(admin.StackedInline):
    formset = AtLeastOneRequiredInlineFormSet
    max = len(settings.LANGUAGES)
    extra = 0


class PageTranslationInline(TranslationInline, CKModelAdminMixin):
    model = PageTranslation


class PageAdmin(VersionAdmin, CKModelAdminMixin):
    inlines = (PageTranslationInline, )


class BaseArticleTranslationInline(TranslationInline, CKModelAdminMixin):
    model = BaseArticleTranslation


class BaseArticleAdmin(VersionAdmin, CKModelAdminMixin):
    inlines = (BaseArticleTranslationInline, )


class ContentTranslationInline(TranslationInline, CKModelAdminMixin):
    prepopulated_fields = {'slug': ('title',)}
    model = ContentTranslation


class MediaItemAdmin(CKMediaItemAdmin):
    inlines = (ContentTranslationInline, )


class MediaCollectionAdmin(admin.ModelAdmin):
    inlines = (ContentTranslationInline, )


class CategoryTranslationInline(TranslationInline):
    prepopulated_fields = {'slug': ('title',)}
    model = CategoryTranslation


class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryTranslationInline, )


admin.site.register(Page, PageAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, BaseArticleAdmin)

admin.site.register(MediaItem)
admin.site.register(MediaCollection, MediaCollectionAdmin)

'''
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin


class ContentChildAdmin(PolymorphicChildModelAdmin, CKModelAdminMixin):
    base_model = Content


class ChildBaseArticleAdmin(BaseArticleAdmin, ContentChildAdmin):
    pass


class ContentAdmin(PolymorphicParentModelAdmin):
    base_model = Content
    child_models = (
        (Article, ContentChildAdmin),
        (Page, ContentChildAdmin),
    )

admin.site.register(Content, ContentAdmin)
'''
