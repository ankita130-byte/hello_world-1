from django.shortcuts import render
from django.http import HttpResponse
def homePageView(request):
    return HttpResponse("Hello, world!, This is my first Git")

# Create your views here.
