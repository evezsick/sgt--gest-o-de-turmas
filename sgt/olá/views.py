from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style=\"color:pink\">Olá, mundo!</h1>")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")