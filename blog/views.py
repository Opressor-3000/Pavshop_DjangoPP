from django.shortcuts import render
from django.http import HttpResponse


def blog_detail(request):
    return HttpResponse("blog_detail.html")

def blog_list(request):
    return HttpResponse("blog_list.html")