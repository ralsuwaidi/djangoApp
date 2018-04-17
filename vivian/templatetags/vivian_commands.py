from django import template
import praw
import markdown2
from django.template.defaultfilters import stringfilter
from vivian.functions import reddit

register = template.Library()

@register.filter
def markdown(value):
    return markdown2.markdown(value)

@register.filter
def populate_reddit(value):
    return reddit()
