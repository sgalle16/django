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
        # Obtiene el valor de busqueda desde la URL
        searchTerm = request.GET.get('searchMovie', '')

        if searchTerm:
            # Filtra películas por el valor de búsqueda
            movies = Movie.objects.filter(title__icontains=searchTerm)
        else:
            movies = Movie.objects.all()

        context = {
            'movies': movies,
            'searchTerm': searchTerm
        }
        return render(request, 'home.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
