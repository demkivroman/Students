# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students
def students_list(request):
    students = (
    {'id':1,
     'first_name': u'Віталій',
     'last_name': u'Подоба',
     'ticket': 235,
     'image': 'img/1111.jpg'},
    {'id':2,
     'first_name': u'Роман',
     'last_name': u'Демків',
     'ticket': 1235,
     'image': 'img/P8270023.JPG'},
    {'id':3,
     'first_name': u'Стів',
     'last_name': u'Джобс',
     'ticket': 555,
     'image': 'img/xwmX0hz291o.jpg'},
    )
    return render(request,'students/students_list.html',{'students': students})




def students_add(request):
    return HttpResponse('<h1>Students AddForm</h1>')

def students_edit(request,sid):
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)

def students_delete(request,sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

