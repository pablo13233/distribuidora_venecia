from django.urls import path
from . import views
from apps.busqueda.views import *

app_name = "busqueda_app"


urlpatterns = [
     path("productosq", busqueda_producto, name="busqueda_producto"),
     path('productos/<int:id_categoria>/',busqueda_categoria, name='busqueda_categoria'),
]