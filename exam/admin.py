from django.contrib import admin
from exam.models import Exam, Topic, Field, ExamHistory

# Register your models here.
admin.site.register([Exam, ExamHistory])