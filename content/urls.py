from django.conf.urls import patterns, url

from .views import ContentListView, ContentDetailView, ArticleDetailView, ArticleListView
from .models import Page, Article, BaseArticle


urlpatterns = patterns(
    '',
    url(
        regex=r'^blog/$',
        view=ContentListView.as_view(model=Article, template_name='content/article_list.html'),
        name='article-list'
    ),
    url(
        regex=r'^blog/category/(?P<category>[\w-]+)/$',
        view=ArticleListView.as_view(model=BaseArticle, template_name='content/article_list.html'),
        name='article-list-by-category'
    ),
    url(
        regex=r'^blog/tag/(?P<tag>[\w-]+)/$',
        view=ArticleListView.as_view(model=BaseArticle, template_name='content/article_list.html'),
        name='article-list-by-tag'
    ),
    url(
        regex=r'^blog/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
        view=ArticleDetailView.as_view(model=BaseArticle),
        name='article-detail'
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

