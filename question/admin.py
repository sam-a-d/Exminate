from django.contrib import admin

from .models import Tag, MCQ
# Register your models here.

admin.site.register([Tag, MCQ])