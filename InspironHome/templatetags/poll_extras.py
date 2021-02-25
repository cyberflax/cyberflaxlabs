from django import template

register = template.Library()
@register.filter
def repspace(value):
    val = value.replace('/','__')
    value = val.replace(' ','_')
    return value