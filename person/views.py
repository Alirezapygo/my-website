from django.shortcuts import render
from django.http import HttpResponse

def abut(request):
    return HttpResponse("<h1>abut<h1/>")
def shop(request):
    return HttpResponse("<h1>shop<h1/>")
def home(request):
    return HttpResponse("<h1>home<h1/>")
