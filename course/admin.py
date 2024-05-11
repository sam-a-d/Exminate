from django.contrib import admin

from .models import Course, CourseVerificationToken, CourseHistory
# Register your models here.
admin.site.register([Course,CourseVerificationToken, CourseHistory])