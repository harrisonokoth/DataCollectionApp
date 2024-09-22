# data_preprocessing/urls.py
from django.urls import path
from django.http import HttpResponse
from . import views

def home(request):
    return HttpResponse("<h1>Welcome to Data Preprocessing Home Page!</h1>")

urlpatterns = [
    path('', home, name='home'),  # Map root URL to home view
]
