from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('Hello World!')


def index(request):
    return HttpResponse('Index page')


def health_check(request):
    return HttpResponse('I am Healthy')
