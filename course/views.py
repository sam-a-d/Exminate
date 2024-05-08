from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Custom Imports
from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = "course/course-catalog.html"

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "course/course-detail.html"
