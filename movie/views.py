from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie


def home(request):
    # return HttpResponse("<h1>Welcome to the Home Page</h1>")
    # return render(request, 'home.html',)
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def about(request):
    return render(request, 'about.html',)
