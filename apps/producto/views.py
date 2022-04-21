from django.shortcuts import render
from django.http import JsonResponse 
from django.contrib.auth.models import User

from apps.marca.models import Marca
from apps.producto.models import Producto
from apps.categoria.models import Categoria

# Create your views here.

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

                pro.usuario = User.objects.get(pk=1)
                pro.save()

                if request.FILES: 
                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(pro.pk)+"_"+imagen.name
                    pro.img_producto = imagen
                    pro.save()#Actualizamos la ruta de la imagen con la concatenacion del id recien creado

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

            elif action == 'eliminar':
                pro = Producto.objects.get(pk=request.POST['id'])
                if pro.img_producto.url != "/media/img_defecto.jpg":
                    pro.img_producto.delete()

                pro.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    elif request.method == 'GET':
        categorias = Categoria.objects.all()
        marcas = Marca.objects.all()
        return render(request, 'producto/crear_producto.html',{'categorias':categorias,'marcas':marcas})
