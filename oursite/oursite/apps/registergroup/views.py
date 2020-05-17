from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'registergroup/index.html')

