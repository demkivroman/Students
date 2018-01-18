# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from ..models  import Students, Group
from django.views.generic import UpdateView, DeleteView
from django.core.urlresolvers import reverse
from ..util import paginate

# class for group delete

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/group_confirm_delete.html'

    def get_success_url(self):
        messages.info(self.request, u'Групу успішно видалено :)')
        return reverse('groups')


#Views for Groups

def groups_list(request):
    groups = Group.objects.all()
    
    order_by = request.GET.get('order_by',default ='title')

    if order_by in ('title','leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse','') == '1':
            groups = groups.reverse() 
    context = {}
    context = paginate(groups, 3, request, context, var_name='groups')

    return render(request,'students/group_list.html',{'groups': context})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Group Edit %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
