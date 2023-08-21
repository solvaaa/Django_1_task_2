from django import template
from config.settings import MEDIA_URL
register = template.Library()


@register.filter(needs_autoescape=True)
def mediapath(text, autoescape=True):
    media_path = f'{MEDIA_URL}{text}'
    return media_path
