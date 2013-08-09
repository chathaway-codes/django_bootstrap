from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_bootstrap_js_tags():
    return ("<script src=\"%sbootstrap/js/bootstrap.js\"></script>" % settings.STATIC_URL)


@register.simple_tag
def get_bootstrap_css_tags():
    return ("<link href=\"%sbootstrap/css/bootstrap.css\" rel=\"stylesheet\">" % settings.STATIC_URL)


@register.simple_tag
def get_bootstrap_less_tags():
    return ("<link rel=\"stylesheet/less\" type=\"text/css\" href=\"%sbootstrap/less/bootstrap.less\" />" % settings.STATIC_URL )
