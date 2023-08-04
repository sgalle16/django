from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1>Welcome to the Home Page</h1>")
    return render(request, 'home.html', {'name': 'Santiago Gallego'})

def about(request):
    return render(request, 'about.html',)