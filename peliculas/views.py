from django.shortcuts import render
from .models import *
from .utils import render_to_pdf

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
    

def pdf_report(request):

    frameworks = Framework.objects.all()

    context = {
        'frameworks': frameworks
    }

    return render_to_pdf(
        'peliculas/reporte.html',
        context
    )