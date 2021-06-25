from django import template
from django.utils.safestring import mark_safe

from dashboard.metrics import get_cpu, get_ram, get_disk
from dashboard.metrics import get_engine_version as engine_version

register = template.Library()

@register.simple_tag
def get_cpu_data():
    return get_cpu()


@register.simple_tag
def get_ram_data():
    return get_ram

@register.simple_tag
def get_disk_data():
    return get_disk

@register.simple_tag
def get_engine_version():
    """
    Simple template tag function that returns Engine's version when called.
    """
    return engine_version()
