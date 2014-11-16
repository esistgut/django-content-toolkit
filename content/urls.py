from django.conf.urls import patterns, url

from .views import ContentDetailView

urlpatterns = patterns('',
    url(r'^(?P<slug>[-_\w]+)/$', ContentDetailView.as_view(), name='content-detail'),
)