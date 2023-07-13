from django.shortcuts import render
from django.http import HttpResponse


def product_detail(request):
    return HttpResponse("product_detail.html")

def product_list(request):
    return HttpResponse("product_list.html")