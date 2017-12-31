# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# model Exams

class Exams(models.Model):
    
    class Meta(object):
        verbose_name=u"Іспит"
        verbose_name_plural=u"Іспити" 

    title = models.CharField(
        max_length = 256,
        blank = False,    
        verbose_name = u"Назва")

    dataTime = models.DateTimeField(
        blank = False,
        verbose_name = u"Дата і час")

    teacher = models.CharField(
        max_length = 256,
        blank = False,
        verbose_name = u"Викладач")

    groups = models.ForeignKey('Group',
        verbose_name = u"Група",
        blank = False,
        null = True,
        on_delete=models.SET_NULL)

    def __unicode__(self):
        return u"%s - %s (%s %s)" % (self.title, self.dataTime, self.teacher, self.groups)
