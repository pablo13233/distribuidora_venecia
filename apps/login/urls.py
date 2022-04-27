from django.urls import path
from . import views
from apps.login.views import *

app_name = "login_app"


urlpatterns = [
     path("login", login, name="login"),
     path("cerrar_sesion", cerrar_sesion, name="cerrar_sesion"),
]