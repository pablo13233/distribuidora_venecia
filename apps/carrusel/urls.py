from django.urls import path
from . import views
from apps.carrusel.views import *


app_name = 'carrusel_app'

urlpatterns = [
    
    path('carrusel-list/', views.CarruselListView.as_view(),name='carrusel_list',
    ),
]

