from django.urls import path
from person.views import *

urlpatterns = [
    path('abut',abut),
    path('shop',shop),
    path('',home)
]