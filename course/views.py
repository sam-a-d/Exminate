from django.shortcuts import render
from django.views.generic.list import ListView

# Custom Imports
from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = "course/couse-catalog.html"
