
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'carrusel_app'

urlpatterns = [
    
    path(
        'carrusel-lista/',
        views.CarruselListView.as_view(),
        name='carrusel_list',
    ),
]

