from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#def index(request):
#    return HttpResponse("Hello, World")

def index(request):
    return render (request, "index.html")

def greet(request, name):
    return render (request, "greet.html", {'name':name})

def gm(request, name):
    day = datetime.now()
    return render (request, "gm.html", {'name':name, 'day': day})

