from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import IntegrationConfigForm

def add_integration_config(request):
    if request.method == 'POST':
        form = IntegrationConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or another appropriate page
    else:
        form = IntegrationConfigForm()
    return render(request, 'llm_integration/add_integration_config.html', {'form': form})

def index(request):
    return render(request, 'llm_integration/index.html')
