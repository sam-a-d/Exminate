from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# custom imports 
from .models import Exam

# Create your views here.
class ExamListView(ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = "exam/exams.html"

class ExamDetailView(DetailView):
    model = Exam
    context_object_name = 'exam'
    template_name = "exam/exam-detail.html"
