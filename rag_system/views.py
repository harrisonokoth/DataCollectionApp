from django.shortcuts import render

def index(request):
    return render(request, 'rag_system/index.html')
