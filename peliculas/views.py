from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'peliculas/home.html')


def languages(request):
    languages = Language.objects.all()

    context = {
        'languages': languages
    }

    return render(
        request,
        'peliculas/languages.html',
        context
    )

def movies(request):
    characters = Character.objects.all()

    context = {
        'characters': characters
    }

    return render(
        request,
        'peliculas/movies.html',
        context
    )
    