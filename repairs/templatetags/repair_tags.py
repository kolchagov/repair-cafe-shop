from django import template

register = template.Library()

BADGE_CLASSES = {
    'fixed': 'text-bg-success',
    'unfixable': 'text-bg-danger',
    'in-progress': 'text-bg-warning',
}


@register.filter
def status_badge(status):
    """Map a ticket status to its Bootstrap badge class."""
    return BADGE_CLASSES.get(status, 'text-bg-secondary')
