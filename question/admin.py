from django.contrib import admin

from .models import Tag, MCQ, ShortQues, LongQues
# Register your models here.

admin.site.register([Tag, MCQ, ShortQues, LongQues])