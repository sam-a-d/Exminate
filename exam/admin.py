from django.contrib import admin
from exam.models import Exam, Topic, Field

# Register your models here.
admin.site.register([Exam, Topic, Field])