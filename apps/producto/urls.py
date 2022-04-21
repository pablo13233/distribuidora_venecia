from django.urls import path
from . import views
from apps.producto.views import *

app_name = "producto_app"


urlpatterns = [
     path("producto/ajax", producto_ajax, name="producto_ajax"),
]