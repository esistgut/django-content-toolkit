from django.views.generic import ListView
from django.views.generic.detail import DetailView

from taggit.models import Tag

from .models import BaseEntryTranslation


class ContentListView(ListView):
    context_object_name = 'contents'


class ContentDetailView(DetailView):
    context_object_name = 'content'
    template_name = 'content/content.html'

    def get_object(self, queryset=None):
        q = self.get_queryset()
        q = q.filter(translations__slug=self.kwargs['slug'])
        return q.get()


class EntryListView(ContentListView):
    context_object_name = 'contents'

    def get_queryset(self):
        q = super().get_queryset()
        if 'category' in self.kwargs:
            q = q.filter(categories__translations__slug=self.kwargs['category'])
        if 'tag' in self.kwargs:
            tags = Tag.objects.filter(slug=self.kwargs['tag'])
            q = q.filter(translations__tags=tags)
        return q


class EntryDetailView(ContentDetailView):
    template_name = 'content/entry.html'

    def get_queryset(self):
        q = super().get_queryset()
        q = q.filter(
            publication_time__year=self.kwargs['year'],
            publication_time__month=self.kwargs['month'],
            publication_time__day=self.kwargs['day'],
        )
        return q
