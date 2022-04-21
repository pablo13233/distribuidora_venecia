from django.shortcuts import render
from django.http import JsonResponse 
from django.contrib.auth.models import User

# Create your views here.
from apps.categoria.models import *




def categoria_ajax (request):
    if request.method == 'POST' and request.is_ajax():
        data = []
        try:
            action = request.POST['action']
            if action == 'buscardatos':
                for i in Categoria.objects.all():
                    data.append(i.toJSON())
            elif action == 'crear':

                ca = Categoria()
                ca.nombre_categoria = request.POST['nombre_categoria']
                ca.descripcion_categoria = request.POST['descripcion']         
                ca.usuario = User.objects.get(pk=1)
                ca.save()

                if request.FILES: 
                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(ca.pk)+"_"+imagen.name
                    ca.img_categoria = imagen
                    ca.save()#Actualizamos la ruta de la imagen con la concatenacion del id recien creado

            elif action == 'editar':

                ca = Categoria.objects.get(pk=request.POST['id'])
                ca.nombre_categoria = request.POST['nombre_categoria']
                ca.descripcion_categoria = request.POST['descripcion']

                if request.FILES:
                    if ca.img_categoria.url != "/media/img_defecto.jpg":
                        ca.img_categoria.delete()

                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(ca.pk)+"_"+imagen.name
                    ca.img_categoria = imagen 

                ca.usuario = User.objects.get(pk=1)
                ca.save()

            elif action == 'eliminar':
                cal = Categoria.objects.get(pk=request.POST['id'])
                if cal.img_categoria.url != "/media/img_defecto.jpg":
                    cal.img_categoria.delete()

                cal.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    elif request.method == 'GET':
        print("Metodo normal")
        return render(request, 'categoria/crear_categoria.html',{'titulo':'Inicio','entidad':'Creacion de categorias'})


