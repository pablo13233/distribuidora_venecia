from itertools import product
from django.shortcuts import render
from django.http import JsonResponse 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required #Manejo de permisos
from django.core.paginator import Paginator #Paginador para html
from django.db.models import Q 

from apps.producto.models import * 
from apps.marca.models import * 
from apps.categoria.models import * 


# Create your views here.
#Vista para renderizar a plantilla busqueda con sus filtros
def busqueda_producto(request):
	if request.method == 'GET':
		consulta = request.GET['busqueda']
		page_number = request.GET.get('page')
		categorias = Categoria.objects.all()
		marcas = Marca.objects.all()

		#filtros de la consulta
		productos = Producto.objects.filter(
			Q(nombre_producto__icontains=consulta)	|
			Q(descripcion_producto__icontains=consulta) |
			Q(categoria__nombre_categoria__icontains=consulta) |
			Q(marca__nombre_marca__icontains=consulta) 
		).distinct().order_by('id')


		#paginador para los resultados
		paginator = Paginator(productos, 6)
		productos = paginator.get_page(page_number)

		data = {'categorias': categorias, 'marcas': marcas,'productos': productos}
		return render(request, 'busqueda/busqueda.html',data)


def busqueda_categoria(request,id_categoria):
	if request.method == 'GET':
		categorias = Categoria.objects.all()
		categoria = Categoria.objects.get(pk=id_categoria)
		productos = Producto.objects.filter(categoria=categoria.pk)
		page_number = request.GET.get('page')
		
		#paginador para los resultados
		paginator = Paginator(productos, 6)
		productos = paginator.get_page(page_number)
		data = {'productos': productos, 'categorias': categorias, 
				'nombre_categoria': categoria.nombre_categoria,
				'id_categoria': id_categoria}
		return render(request, 'busqueda/busqueda.html',data)