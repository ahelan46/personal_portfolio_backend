from django import template

register = template.Library()

@register.filter
def split(value, sep=','):
    """Split a string by `sep` and return a list with whitespace stripped."""
    if not value:
        return []
    try:
        return [part.strip() for part in value.split(sep)]
    except Exception:
        return []
