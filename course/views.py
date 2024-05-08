from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Custom Imports
from .models import Course
from exam.models import Exam

# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = "course/course-catalog.html"

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "course/course-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exams'] = Exam.objects.filter(course=self.kwargs.get('pk'))
        return context