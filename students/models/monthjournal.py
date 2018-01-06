# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from .students import Students

# Create your models here.

class MonthJournal(models.Model):
      #Student Model
    class Meta:
        verbose_name=u"Місячний Журнал"
        verbose_name_plural=u"Місячні журнали"

    student = models.ForeignKey(Students,
        verbose_name = u"Студент",
        blank = False,
        unique_for_month = 'date')

    date = models.DateField(
        verbose_name = u"Дата",
        blank = False,
        )
    
    def __unicode__(self):
        return u"%s: %d, %d" % (self.student.last_name, self.date.month, self.date.year)




