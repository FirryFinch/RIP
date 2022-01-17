from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Movie, Platform


def index(request):
    movies = Movie.objects.all()
    platforms = Platform.objects.all()
    return render(request, "index.html", {"movies": movies, "platforms": platforms})

def report(request):
    movies = Movie.objects.all()
    platforms = Platform.objects.all()
    return render(request, "report.html", {"movies": movies, "platforms": platforms})

def create_movie(request):
    if request.method == "POST":
        m = Movie()
        m.name = request.POST.get("name")
        m.description = request.POST.get("description")
        m.rating = request.POST.get("rating")
        m.platform = Platform.objects.get(name=request.POST.get("platform"))
        m.save()
    return HttpResponseRedirect("/report/")

def create_platform(request):
    if request.method == "POST":
        p = Platform()
        p.name = request.POST.get("name")
        p.site = request.POST.get("site")
        p.save()
    return HttpResponseRedirect("/report/")


def edit_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)

        if request.method == "POST":
            movie.name = request.POST.get("name")
            movie.description = request.POST.get("description")
            movie.rating = request.POST.get("rating")
            movie.platform = Platform.objects.get(name=request.POST.get("platform"))
            movie.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_movie.html", {"movie": movie})
    except Movie.DoesNotExist:
        return HttpResponseNotFound("<h2>Movie is not found</h2>")


def edit_platform(request, id):
    try:
        platform = Platform.objects.get(id=id)

        if request.method == "POST":
            platform.name = request.POST.get("name")
            platform.site = request.POST.get("site")
            platform.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_platform.html", {"platform": platform})
    except Platform.DoesNotExist:
        return HttpResponseNotFound("<h2>Platform not found</h2>")


def delete_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
        movie.delete()
        return HttpResponseRedirect("/report/")
    except Movie.DoesNotExist:
        return HttpResponseNotFound("<h2>Movie not found</h2>")


def delete_platform(request, id):
    try:
        platform = Platform.objects.get(id=id)
        platform.delete()
        return HttpResponseRedirect("/report/")
    except Platform.DoesNotExist:
        return HttpResponseNotFound("<h2>Platform not found</h2>")