from django.shortcuts import render
from django.views.generic import ListView

# custom imports 
from .models import Exam

# Create your views here.
class CourseListView(ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = "exam/exams.html"
