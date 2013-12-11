from django import template
register = template.Library()
@register.filter(name='is_false')
def is_false(value):
  return value is False