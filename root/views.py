from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def student_dashboard(request):
    return render(request,"studashboard.html")



def teacher_dashboard(request):
    return render(request,"teacherdashboard.html")




def examinatelogin(request):
    return render(request,"login.html")


def examinatesignup(request):
    return render(request,"signup.html")