from django import template

from engine import VERSION

register = template.Library()

@register.simple_tag
def get_engine_version():
    return VERSION