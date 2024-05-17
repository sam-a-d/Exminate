from django import template

register = template.Library()

@register.simple_tag
def sum_numbers(*args):
    args = tuple(float(i) for i in args)
    return sum(args)

