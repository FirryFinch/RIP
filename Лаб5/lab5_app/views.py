from django.shortcuts import render

# Create your views here.

from lab5_app.models import Movie
from lab5_app.models import Platform


def MovieList(request):
    return render(request, 'movielist.html', {'data': {
        'platforms': Platform.objects.all(),
        'movies': Movie.objects.all(),
    }})


def GetPlatform(request, id):
    return render(request, 'platform.html', {'data': {
        'platform': Platform.objects.filter(id=id)[0]
    }})


def GetMovie(request, id):
    return render(request, 'movie.html', {'data': {
        'movie': Movie.objects.filter(id=id)[0],
        'platforms': Platform.objects.all(),
    }})

