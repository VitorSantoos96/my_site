from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('LOGIN AND REGISTRER')


def registrer(request):
    return HttpResponse('REGISTRER')

def login(request):
    return HttpResponse('LOGIN')
