from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static

from sorl.thumbnail import get_thumbnail


class CKModelAdmin(object):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }

    class Media:
        js = [
            static('content/ckeditor/ckeditor.js'),
            static('content/ckeditor_setup.js'),
        ]

        css = {
            'all': (static('content/ckeditor_style_override.css'),)
        }


class CKMediaItemAdmin(admin.ModelAdmin, CKModelAdmin):
    prepopulated_fields = {'title': ('file',), 'slug': ('file',) }

    list_display = ('thumbnail', 'file', 'title')

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
