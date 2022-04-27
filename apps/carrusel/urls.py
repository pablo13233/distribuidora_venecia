from django.urls import path
from . import views
from apps.carrusel.views import *


app_name = 'carrusel_app'

urlpatterns = [
    
    path('gestion_carrusel/ajax', gestion_carrusel_ajax, name='gestion_carrusel_ajax',
    ),
]
