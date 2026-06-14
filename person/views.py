from django.shortcuts import render
from django.http import HttpResponse

def abut(request):
    return render(request,'websit/abut.html')
def shop(request):
    return render(request, 'websit/shop.html')
def home(request):
    return render(request,'websit/index.html')
