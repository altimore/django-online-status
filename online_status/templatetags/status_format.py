from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.filter(name='status_format')
def status_format(val, arg="text"):
    if arg == "text":
        if val == 1:
            return _('Online')
        elif val == 0:
            return _('Idle')
        else:
            return _('Offline')
    elif arg == "tag":
        if val == 1:
            return 'Online'
        elif val == 0:
            return 'Idle'
        else:
            return 'Offline'
    else:
        return val
