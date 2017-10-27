# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

#Views for Groups

def groups_list(request):
    groups = (
    {'id':1,
     'name':u'МТМ-21',
     'lider':u'Демків Роман'},
    {'id':2,
     'name':u'МТН-25',
     'lider':u'Демків Тарас'},
    {'id':3,
     'name':u'МТГ-2123',
     'lider':u'Цукерберг Марк'},
    )
    return render(request,'students/group_list.html',{'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Group Edit %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
