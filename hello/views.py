from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("hello_world Python demo App")
