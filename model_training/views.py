from django.shortcuts import render

def index(request):
    return render(request, 'model_training/index.html')
