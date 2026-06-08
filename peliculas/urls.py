from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('languages/', views.languages, name='languages'),
    path('movies/', views.movies, name='movies'),
    path('pdf/', views.pdf_report, name='pdf_report'),
    path('email/', views.send_email, name='send_email'),
]