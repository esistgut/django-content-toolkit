from django import template

from ..models import Content, Entry


register = template.Library()


@register.assignment_tag()
def content(slug):
    return Content.objects.get(translations__slug=slug)


@register.assignment_tag()
def entries():
    return Entry.objects.all()


@register.assignment_tag()
def random_item(items):
    return items.order_by('?').first()