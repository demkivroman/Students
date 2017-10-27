# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

#View for visiting

def journal_form(request):
    return render(request,'students/visiting.html',{})
