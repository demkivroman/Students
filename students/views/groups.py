# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from ..models import Group

#Views for Groups

def groups_list(request):
    groups = Group.objects.all()
    
    order_by = request.GET.get('order_by',default ='title')

    if order_by in ('title','leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            groups = groups.reverse() 

    onPage = 3   
    
    page = int(request.GET.get('page', default = 1))-1
    
    subGroupList = []
    groupList = []
    pages = []
    i = 0
    p = 1 
    for group in groups:
        if i < onPage:
            subGroupList.append(group)
            i += 1
        else:
            groupList.append(subGroupList)
            pages.append(p)
            p += 1
            subGroupList = []
            i = 1
            subGroupList.append(group)
    if len(subGroupList) > 0:
        groupList.append(subGroupList)
        pages.append(p) 

  #class for passing parrameters to tample
    class GroupsList:
        def __init__(self, pages, pagesList):
            self.pages = pages
            self.pagesList = pagesList  
            self.lastPage = len(pages)
            self.number = page + 1  

    if len(groupList) > 0:
        obj = GroupsList(pages,groupList[page])  
    else:
        obj = GroupsList(pages,groups)      
    

    return render(request,'students/group_list.html',{'groups': obj})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Group Edit %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
