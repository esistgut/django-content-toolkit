from django import template

from ..models import Content


register = template.Library()


@register.assignment_tag()
def content(slug):
    return Content.objects.get(translations__slug=slug)