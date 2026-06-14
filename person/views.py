from django.shortcuts import render
from django.http import HttpResponse

def abut(request):
    return render(request,'website/abut.html')
def shop(request):
    return render(request, 'website/shop.html')
def home(request):
    return render(request,'website/index.html')
