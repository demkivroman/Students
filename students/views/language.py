from django.utils import translation
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def switch_lang(request):
    lang = request.COOKIES.get('current_language')
    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
