from django.contrib import admin

from .models import Topic, Field, Institute, Department, Semester, Designation,Teacher
# Register your models here.
admin.site.register([Topic, Field, Institute, Department, Semester, Designation,Teacher])