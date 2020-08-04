from django.shortcuts import HttpResponse

# Create your views here.

def home(requets):
    return HttpResponse('Hello, World')