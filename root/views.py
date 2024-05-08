from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """View for homepage"""
    return render(request, 'home.html')

def student_dashboard(request):
    """View for Student Dashboard"""
    return render(request,"studashboard.html")

def teacher_dashboard(request):
    """View for teachers dashboard"""
    return render(request,"teacherdashboard.html")

def examinatelogin(request):
    """Login Page"""
    return render(request,"login.html")

def examinatesignup(request):
    """signup page"""
    return render(request,"signup.html")