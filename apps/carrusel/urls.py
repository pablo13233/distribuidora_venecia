from django.urls import path
from . import views
from apps.carrusel.views import *


app_name = 'carrusel_app'

urlpatterns = [
    
    path('carrusel-lista/', views.CarruselListView.as_view(),name='carrusel_list',
    ),
]

urlpatterns = [
    
    path('gestion_carrusel/ajax', gestion_carrusel_ajax, name='gestion_carrusel_ajax',
    ),
]