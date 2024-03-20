from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


############################### Define filters
@register.filter(name="cut")
@stringfilter
def cut(value, arg):
    """
    Removes all values of arg from the given string
    Use like this --> {{ somevariable|cut:"0" }}
    """
    return value.replace(arg, "")
