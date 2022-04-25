from django.urls import path
from . import views
from apps.producto.views import *

app_name = "producto_app"


urlpatterns = [
     path("producto/ajax", producto_ajax, name="producto_ajax"),
     path("producto/<pk>", views.ProductDetailView.as_view(), name='producto_detail'),
     path('producto-lista', views.ProductoLastList.as_view(), name='producto_list'),
     path('productos', views.ProductosListView.as_view(), name='producto_all'),
]