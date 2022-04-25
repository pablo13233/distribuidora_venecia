from django.urls import path
from . import views
from apps.categoria.views import *

app_name = "categoria_app"


urlpatterns = [
     path("categoria/ajax", categoria_ajax, name="categoria_ajax"),
     path('categoria', categoriaList, name="categoria_list"),
]