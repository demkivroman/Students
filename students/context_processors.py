from .util import get_groups
from django.utils import translation

def groups_processor(request):
    return {
        'GROUPS': get_groups(request),
        'LANGUAGE_CODE': translation.get_language()
    }
