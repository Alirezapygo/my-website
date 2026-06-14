from django.urls import path
from person.views import abut,shop,home

urlpatterns = [
    path('abut',abut),
    path('shop',shop),
    path('',home)
]