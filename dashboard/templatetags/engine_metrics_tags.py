from django import template
from django.utils.safestring import mark_safe

from dashboard.metrics import get_cpu, get_ram, get_disk
from dashboard.metrics import get_engine_version as engine_version
from dashboard.metrics import get_sentry_release as sentry_release
from dashboard.metrics import get_sentry_dsn as sentry_dsn

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

@register.simple_tag()
def get_sentry_release():
    """Gets the Sentry release name from settings.py"""
    return sentry_release()

@register.simple_tag()
def get_sentry_dsn():
    """Gets the Sentry DSN from settings.py"""
    return sentry_dsn()
