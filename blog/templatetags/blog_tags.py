from django import template
from django.conf import settings

register = template.Library()

title = ""
featured_img_url = ""
subtitle = ""

@register.simple_tag
def set_featured_img_url(val=None):
    global featured_img_url
    featured_img_url = val
    return True

@register.simple_tag
def get_featured_img_url():
    global featured_img_url
    this_featured_img_url = featured_img_url
    featured_img_url = None
    return this_featured_img_url

@register.simple_tag
def set_title(val=None):
    global title
    title = val
    return True

@register.simple_tag
def get_title():
    global title
    this_title = title
    title = None
    return this_title

@register.simple_tag
def set_subtitle(val=None):
    global subtitle
    subtitle = val
    return True

@register.simple_tag
def get_subtitle():
    global subtitle
    this_subtitle = subtitle
    subtitle = None
    return this_subtitle

@register.simple_tag
def experimental_comments_status():
    commenting_status = settings.ENABLE_EXPERIMENTAL_BLOG_COMMENTING
    return commenting_status
