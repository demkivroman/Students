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
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from django.views.i18n import JavaScriptCatalog
from students.views import students
from students.views import groups
from students.views import journal
from students.views import stud_test
from students.views import exams
from students.views import language
from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView,StudentDeleteView
from students.views.groups import GroupDeleteView, groups_list, groups_add, groups_edit
from students.views.journal import JournalView

from django.conf import settings
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

js_info_dict = {
    'packages': ('students',),
}

urlpatterns = [
#Students url
    url(r'^$',students.students_list, name='home'),
    url(r'^students/add$',students.students_add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',StudentUpdateView.as_view(),name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',StudentDeleteView.as_view(),name='students_delete'),
    url(r'^language/$',language.switch_lang, name='language'),

    url(r'^test$',stud_test.students_test, name='test'),
#Groups url
    url(r'^groups$',login_required(groups_list),name='groups'),
    url(r'^groups/add$',login_required(groups_add),name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$',login_required(groups_edit),name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',login_required(GroupDeleteView.as_view()),name='groups_delete'),
#Visiting url
    url(r'^journal/(?P<pk>\d+)?/?$',JournalView.as_view(),name='journal'),
#Emams url
    url(r'^exams/$',exams.exams_list,name='exams'),
# Contact Admin Form
    url(r'^contact/$', ContactView.as_view(), name = 'contact_admin'),
# urls for login
    url(r'^users/profile/$', login_required(TemplateView.as_view(
                 template_name='registration/profile.html')), name = 'profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'home'}, name = 'auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name ='home'), name = 'registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
#Admin url
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^jsi18n/$',JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
