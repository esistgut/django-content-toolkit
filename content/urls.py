from django.conf.urls import patterns, url

from .views import ContentListView, ContentDetailView, EntryDetailView, EntryListView
from .models import Page, Entry, BaseEntry


urlpatterns = patterns(
    '',
    url(
        regex=r'^blog/$',
        view=ContentListView.as_view(model=BaseEntry, template_name='content/entry_list.html'),
        name='entry-list'
    ),
    url(
        regex=r'^blog/category/(?P<category>[\w-]+)/$',
        view=EntryListView.as_view(model=BaseEntry, template_name='content/entry_list.html'),
        name='entry-list-by-category'
    ),
    url(
        regex=r'^blog/tag/(?P<tag>[\w-]+)/$',
        view=EntryListView.as_view(model=BaseEntry, template_name='content/entry_list.html'),
        name='entry-list-by-tag'
    ),
    url(
        regex=r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-]+)/$',
        view=EntryDetailView.as_view(model=BaseEntry),
        name='entry-detail'
    ),
    url(
        regex=r'^(?P<slug>[-_\w]+)/$',
        view=ContentDetailView.as_view(model=Page),
        name='page-detail'
    ),
    url(
        regex=r'^(?P<slug>[-_\w]+)/$',
        view=ContentDetailView.as_view(),
        name='content-detail'
    ),
)

