# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.core.urlresolvers import reverse

from ..models import MonJournal, Students
from ..util import paginate, get_current_group
from django.http import JsonResponse


#View for visiting

class JournalView(TemplateView):
    template_name = "students/journal.html"

    def post(self, request, *args, **kwargs):
        data = request.POST
        
        # prepare student, dates and presence data

        current_date = datetime.strptime(data['date'],'%Y-%m-%d').date()
        month = date(current_date.year, current_date.month, 1)
        present = data['present'] and True or False
        student = Students.objects.get(pk=data['pk'])
     
        
        # get or create journal object for given student and month
        journal = MonJournal.objects.get_or_create(student = student, date = month)[0]

        # set new presence on journal for given student and save result
        setattr(journal, 'present_day%d' % current_date.day, present)
        journal.save()              
        """import pdb; pdb.set_trace()"""
        return JsonResponse({'key': 'success'})

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(JournalView, self).get_context_data(**kwargs)
        
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'],'%Y-%m-%d').date()
        else:           
            today = datetime.today()
            month = date(today.year, today.month, 1)
        
        # обчислюємо поточний рік, попередній і наступний місяці
        next_month = month + relativedelta(months=1)
        prev_month = month - relativedelta(months=1)
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['cur_month'] = month.strftime('%Y-%m-%d')
        context['month_verbose'] = month.strftime('%B')

        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear,mmonth)[1]
        context['month_header'] = [{'day':d, 'verbose':day_abbr[weekday(myear,mmonth,d)][:2]}
            for d in range(1, number_of_days+1)] 
        # витягуємо усіх студентів посортованих по прізвищу
        # або одного, якщо нам потрібно показати його журнал відвідування
        
        if kwargs.get('pk'):
            queryset = [Students.objects.get(pk=kwargs['pk'])]
        else:     
            queryset = Students.objects.order_by('last_name')

        # це адреса для посту AJAX запиту, як бачите, ми робитимемо його на цю ж в'юшку 
        # вюшка журналу буде і показувати журнал і обслуговувати запити 
        # типу пост на оновлення журналу;

        update_url = reverse('journal') 

        # пробігаємось по усіх студентах і збираємо 
        # необхідні дані:

        students = []
        journals = []
        for student in queryset:
            # TODO:витягуємо журнал для студента із вибраного місця
            # набиваємо дні для студента
            try:
                journal = MonJournal.objects.get(student=student,date=month)
            except Exception:
                journal = None
            # fill in days presence list for current student  
            journals.append(journal)
            days = []
            for day in range(1, number_of_days+1):
                days.append({
                    'day':day,
                    'present': getattr(journal,'present_day%d' % day, False),
                    'date': date(myear,mmonth,day).strftime('%Y-%m-%d'),})
            # набиваємо усі решта дані студента
                
            students.append({
                'fullname': u'%s %s' % (student.last_name,student.first_name),
                'days': days,
                'id': student.id,
                'update_url': update_url})

        # застосовуємо пагінацію до списку студентів
        context = paginate(students, 10, self.request, context, var_name='students')
        
        # повертаємо оновлений словник із даними
        return context          
        
         
