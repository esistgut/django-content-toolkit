from django.views.generic.detail import DetailView

from .models import AbstractContent


class ContentDetailView(DetailView):
    context_object_name = 'content'
    model = AbstractContent

    def get_template_names(self):
        return self.object.get_template()