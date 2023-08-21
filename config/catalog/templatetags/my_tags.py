from django import template

register = template.Library()

@register.filter(needs_autoescape=True)
def mediapath(text, autoescape=True):
    media_path = f'/media/{text}'
    return media_path