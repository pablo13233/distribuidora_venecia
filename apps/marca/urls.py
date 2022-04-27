from django.urls import path
from . import views
from apps.marca.views import *

app_name = "marca_app"


urlpatterns = [
     path("marca/ajax", marca_ajax, name="marca_ajax"),
]