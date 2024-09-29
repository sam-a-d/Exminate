from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Custom imports
from course.models import CourseHistory
from exam.models import ExamHistory
from .forms import LoginForm

from .decorators import allowed_user_groups
# Create your views here.

def home(request):
    """View for homepage"""
    return render(request, 'home.html')

@login_required(login_url='login')
def student_dashboard(request):
    """View for Student Dashboard"""
    user = request.user
    courses_taken_by_user = CourseHistory.objects.filter(user=user)
    completed_exams = ExamHistory.objects.filter(user=user)

    context = {
        "courses_taken" : courses_taken_by_user,
        "completed_exams" : completed_exams,
    }

    return render(request,"studashboard.html", context=context)

@allowed_user_groups(allowed_groups=['teacher'])
def teacher_dashboard(request):
    """View for teachers dashboard"""
    return render(request,"teacherdashboard.html")

def examinatelogin(request):
    """Login Page"""

    loginForm = LoginForm()

    context = {
        'loginForm' : loginForm
    }

    return render(request,"login.html", context=context)

def examinatesignup(request):
    """signup page"""
    return render(request,"signup.html")