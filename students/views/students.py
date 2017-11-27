# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from ..models.students import Students

	
# Views for Students
def students_list(request):
    students = Students.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', 'last_name')
    
    if order_by in ('photo','last_name','first_name','ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            students = students.reverse() 

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
    
    if len(studList) > 0:
        obj = StudentsList(pages,studList[page])  
    else:
        obj = StudentsList(pages,students)      
    
    
    return render(request,'students/students_list.html',{'students': obj})




def students_add(request):
    return HttpResponse('<h1>Students AddForm</h1>')

def students_edit(request,sid):
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)

def students_delete(request,sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

