# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Students
from .models import Group
# Register your models here.

admin.site.register(Students)
admin.site.register(Group)
