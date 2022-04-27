
from django.shortcuts import render
from django.views.generic import (
    TemplateView
)

from apps.producto.models import Producto
from apps.carrusel.models import Carrusel

# Create your views here.

class IndexHomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = Producto.objects.all().order_by('-pk')[:8]
        carrusel = Carrusel.objects.filter(estado_Carrusel=True)
        context['imagenes_carrusel'] = carrusel
        context['last_productos'] = productos
        return context

class DashboardIndexView(TemplateView):
    template_name = "dashboard/dashboard_index.html"

