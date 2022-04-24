from pyexpat import model
from re import template
import django
from django.shortcuts import render
from django.views.generic import(ListView,CreateView,TemplateView,UpdateView,DetailView,DeleteView)

# Create your views here.
from .models import Carrusel

class CarruselListView(ListView):
    template_name = 'carrusel/gestion_carrusel.html'
    model = Carrusel
    context_object_name = 'carrusels'



