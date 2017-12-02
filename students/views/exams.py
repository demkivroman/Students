# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from ..models.model_exams import Exams
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Views for Groups

def exams_list(request):
    exams = Exams.objects.all()
    
    order_by = request.GET.get('order_by',default ='dataTime')

    if order_by in ('dataTime','teacher'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            exams = exams.reverse() 

# Paginate exams
  
    paginator = Paginator(exams,3)
    page = request.GET.get('page')
    
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)

    return render(request,'students/exams.html',{'exams': exams})
