from django import template
from catalog.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('catalog/list_categories.html')
def show_categories():
    category = Category.objects.all()
    return {'category': category}