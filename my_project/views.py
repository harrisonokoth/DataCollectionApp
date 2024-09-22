from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Project Home Page!</h1>")
