from django import template
from config.settings import MEDIA_URL


register = template.Library()


@register.filter(needs_autoescape=True)
def mediapath(text, autoescape=True):
    media_path = f'{MEDIA_URL}{text}'
    return media_path


@register.filter
def get_obj_by_pk(obj, key):
    return obj[key]


@register.simple_tag
def mediapath(text):
    return f'{MEDIA_URL}{text}'