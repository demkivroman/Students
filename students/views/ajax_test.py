# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class ajax_test(TemplateView):
    template_name = "students/test.html"

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(ajax_test, self).get_context_data(**kwargs)
        context['value'] = "Hello Ajax"
        context['url'] = reverse('journal')

        return context
    
