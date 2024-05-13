from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Custom imports
from course.models import CourseHistory

# Create your views here.

def home(request):
    """View for homepage"""
    return render(request, 'home.html')

def student_dashboard(request):
    """View for Student Dashboard"""
    user = request.user
    courses_taken_by_user = CourseHistory.objects.filter(user=user)

    context = {
        "courses_taken" : courses_taken_by_user,
    }

    return render(request,"studashboard.html", context=context)

def teacher_dashboard(request):
    """View for teachers dashboard"""
    return render(request,"teacherdashboard.html")

def examinatelogin(request):
    """Login Page"""
    return render(request,"login.html")

def examinatesignup(request):
    """signup page"""
    return render(request,"signup.html")