from django.urls import path
from . import views
from apps.producto.views import *

app_name = "producto_app"


urlpatterns = [
     path("producto/ajax", producto_ajax, name="producto_ajax"),
     path("producto/<pk>", views.ProductDetailView.as_view(), name='producto_detail'),
     path('productos', views.ProductosListView.as_view(), name='producto_all'),
     path('productos-categoria/<int:pk>', views.ProductosByCategoriaListView.as_view(), name='producto_categoria'),
]