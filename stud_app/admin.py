from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser)
admin.site.register([Course, Session_Year, Subject])
admin.site.register([Staff, Staff_Notification, Staff_Leave, Staff_Feedback])
admin.site.register([Student, Student_Notification, Student_Feedback])