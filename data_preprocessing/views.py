from django.shortcuts import render

def index(request):
    return render(request, 'data_preprocessing/index.html')
