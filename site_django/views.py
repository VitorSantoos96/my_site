from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'site_django/pages/home.html')


def registrer(request):
    return render(request, 'site_django/pages/registrer.html')

def login(request):
    return render(request, 'site_django/pages/login.html')
