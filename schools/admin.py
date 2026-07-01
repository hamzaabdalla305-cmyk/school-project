from django.contrib import admin
from .models import Tenant, User, Student, Subject, Grade

admin.site.register(Tenant)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)