from django.shortcuts import render

def index(request):
    return render(request, 'llm_integration/index.html')
