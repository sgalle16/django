from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Movie


"""def home(request):
    # return HttpResponse("<h1>Welcome to the Home Page</h1>")
    # return render(request, 'home.html',)
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})"""


class HomeView(View):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all
        context = {
            'movies': movies
        }
        return render(request, 'home.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
