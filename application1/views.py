from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return HttpResponse('ashok')

def hello(request):
    return HttpResponse('<h1>welcome to my first application program</h1>')