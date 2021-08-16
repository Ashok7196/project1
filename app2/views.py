from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_welcome(request):
    return HttpResponse('this is my second app')