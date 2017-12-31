"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  url, include
from django.contrib import admin


from students.views import students
from students.views import groups
from students.views import journal
from students.views import stud_test
from students.views import exams
from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView,StudentDeleteView
#from .settings import MEDIA_ROOT, DEBUG

from django.conf import settings
from django.views.static import serve


urlpatterns = [
#Students url
    url(r'^$',students.students_list, name='home'),
    url(r'^students/add$',students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',StudentUpdateView.as_view(),name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',StudentDeleteView.as_view(),name='students_delete'),

    url(r'^test$',stud_test.students_test, name='test'),
#Groups url
    url(r'^groups/$',groups.groups_list,name='groups'),
    url(r'^groups/add$',groups.groups_add,name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$',groups.groups_edit,name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$',groups.groups_delete,name='groups_delete'),
#Visiting url
    url(r'^journal/$',journal.journal_form,name='journal'),
#Emams url
    url(r'^exams/$',exams.exams_list,name='exams'),
# Contact Admin Form
    url(r'^contact/$', ContactView.as_view(), name = 'contact_admin'),
#Admin url
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
