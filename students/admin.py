# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models.students import Students
from .models.groups import Group
from .models.model_exams import Exams
# Register your models here.

admin.site.register(Students)
admin.site.register(Group)
admin.site.register(Exams)
