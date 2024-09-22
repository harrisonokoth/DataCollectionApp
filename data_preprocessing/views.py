from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'data_preprocessing/index.html')

def home(request):
    return HttpResponse("Hi, welcome home !.")
