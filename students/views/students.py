# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from ..models  import Students, Group

	
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

    # Якщо форма була запощена
    if request.method == "POST":
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}
            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}
             
            # validate user input 
            first_name = request.POST.get('first_name','').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name','').strip()
            if not last_name:
                errors['last_name'] = u"Прізвища є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception as ex:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1986-04-05)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket','').strip()
            if not ticket:
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group','').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                f = photo.read()
                photoExten = ('.jpeg','.gif','.bmp','.tiff','.png','.jpg')
                extension = os.path.splitext(str(photo))[1].lower()
                if extension in photoExten:  
                    if len(f) > 2000000:
                        errors['photo'] = u"Файл більший 2Mb"
                    else:
                        data['photo'] = photo
                else:
                    errors['photo'] = u"Файл невідповідає формату фотогріфії"                  

            if not errors:
                # create student object
                student = Students(**data)
                student.save()    
                # save to message 
                messages.success(request, u'Студента - %s %s %s, успішно додано :)' % (last_name,first_name,
                request.POST.get('middle_name')))                     
                # redirect user to student list
                return HttpResponseRedirect(reverse('home'))  
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                    {'groups':Group.objects.all().order_by('title'),
                     'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # add to message
            messages.info(request, u'Додавання студента скасовано :)')
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))

    else:
        return render(request,'students/students_add.html',
            {'groups':Group.objects.all().order_by('title')}) 

def students_edit(request,sid):
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)

def students_delete(request,sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

