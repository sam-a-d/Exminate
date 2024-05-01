from django.contrib import admin

from .models import Topic, Field, Teacher
# Register your models here.
admin.site.register([Topic, Field, Teacher])