from django import template

register = template.Library()

@register.simple_tag
def cycle_background_color(counter):
    colors = ['one', 'two', 'three', 'four']  # List of background colors
    return colors[counter % len(colors)]


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)