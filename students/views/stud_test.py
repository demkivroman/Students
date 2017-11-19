# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from ..models import Students

# Views for Students
def students_test(request):   
    students = Students.objects.all()
    onPage = 3    
    page = int(request.GET.get('page', default = 1))-1
    
    subStudList = []
    studList = []
    pages = []
    i = 0
    p = 1 
    for stud in students:
        if i < onPage:
            subStudList.append(stud)
            i += 1
        else:
            studList.append(subStudList)
            pages.append(p)
            p += 1
            subStudList = []
            i = 1
            subStudList.append(stud)
    if len(subStudList) > 0:
        studList.append(subStudList)
        pages.append(p) 

  #class for passing parrameters to tample
    class StudentsList:
        def __init__(self, pages, pagesList):
            self.pages = pages
            self.pagesList = pagesList  
            self.lastPage = len(pages)
            self.number = page + 1   
         
    return render(request,'students/test.html',{'tample_value_students':StudentsList(pages,studList[page])})
