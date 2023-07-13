from django.shortcuts import render
from django.http import HttpResponse


def about_us(request):
    return HttpResponse("about_us.html")

def contact(request):
    return HttpResponse("contact.html")

def index(request):
    return HttpResponse("index.html")