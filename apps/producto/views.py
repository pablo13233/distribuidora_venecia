import re
from django.shortcuts import render
from django.http import JsonResponse 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required #Manejo de permisos

from apps.marca.models import Marca
from apps.producto.models import Producto
from apps.categoria.models import Categoria

#importacion para clases de
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.
@login_required	
def producto_ajax (request):
    if request.method == 'POST' and request.is_ajax():
        data = []
        try:
            action = request.POST['action']
            if action == 'buscardatos':
                for i in Producto.objects.all():
                    data.append(i.toJSON())
            elif action == 'crear':

                pro = Producto()
                pro.nombre_producto = request.POST['nombre_producto']
                pro.descripcion_producto = request.POST['descripcion']
                pro.categoria = Categoria.objects.get(pk=request.POST['id_categoria'])

                if int(request.POST['id_marca']) > 0:
                    pro.marca = Marca.objects.get(pk=request.POST['id_marca'])

                pro.usuario = User.objects.get(pk=request.user.id)
                pro.save()

                if request.FILES: 
                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(pro.pk)+"_"+imagen.name
                    pro.img_producto = imagen
                    pro.save()#Actualizamos la ruta de la imagen con la concatenacion del id recien creado
                data = {'tipo_accion': 'crear','correcto': True}

            elif action == 'editar':

                pro = Producto.objects.get(pk=request.POST['id'])
                pro.nombre_producto = request.POST['nombre_producto']
                pro.descripcion_producto = request.POST['descripcion']
                pro.categoria = Categoria.objects.get(pk=request.POST['id_categoria'])

                if request.FILES:
                    if pro.img_producto.url != "/media/img_defecto.jpg":
                        pro.img_producto.delete()

                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(pro.pk)+"_"+imagen.name
                    pro.img_producto = imagen 


                if int(request.POST['id_marca']) > 0:
                    pro.marca = Marca.objects.get(pk=request.POST['id_marca'])

                
                pro.save()
                data = {'tipo_accion': 'editar','correcto': True}

            elif action == 'eliminar':
                pro = Producto.objects.get(pk=request.POST['id'])
                if pro.img_producto.url != "/media/img_defecto.jpg":
                    pro.img_producto.delete()

                pro.delete()
                data = {'tipo_accion': 'eliminar','correcto': True}
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            data = {'tipo_accion': 'error','correcto': False, 'error': str(e)}

        return JsonResponse(data, safe=False)
    elif request.method == 'GET':
        categorias = Categoria.objects.all()
        marcas = Marca.objects.all()
        return render(request, 'producto/crear_producto.html',{'categorias':categorias,'marcas':marcas})

# clases par vistas
class ProductoLastList(TemplateView):
    template_name = 'producto/producto_last.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all().order_by('-pk')[:8]
        return context


class ProductosListView(ListView):
    template_name = "producto/productos_all.html"
    model = Producto
    paginate_by = 12
    ordering = 'nombre_producto'
    context_object_name = 'productos'
    
    def get_queryset(self):
        palabra = self.request.GET.get('kword', '')
        lista = Producto.objects.filter(
            nombre_producto__icontains=palabra
        )
        return lista




class ProductDetailView(DetailView):
    model = Producto
    template_name = 'producto/producto_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['producto'] = Producto.objects.get(pk=self.kwargs['pk'])
        return context
