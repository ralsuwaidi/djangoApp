from django import template
import praw
import markdown2
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def markdown(value):
    return markdown2.markdown(value)
