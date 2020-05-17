from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')

def timetable(request):
    courses = Course.objects.all()
    return render(request, 'login/timetable.html', {'courses':courses})
