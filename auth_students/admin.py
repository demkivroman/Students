from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User

from .models import SProfile


class StProfileInline(admin.StackedInline):
    model = SProfile

class UserAdmin(auth_admin.UserAdmin):
    inlines = (StProfileInline,)

# replace existing User admin form
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
