from django.shortcuts import render
from django.http import HttpResponse


def checkout(request):
    return HttpResponse("checkout.html")

def login(request):
    return HttpResponse("login.html")

def register(request):
    return HttpResponse("register.html")

def shopping_cart(request):
    return HttpResponse("shopping_cart.html")

