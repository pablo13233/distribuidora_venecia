from django.shortcuts import render
from django.http import JsonResponse 
from django.contrib.auth.models import User

# Create your views here.
from apps.marca.models import *




def marca_ajax (request):
    if request.method == 'POST' and request.is_ajax():
        data = []
        try:
            action = request.POST['action']
            if action == 'buscardatos':
                for i in Marca.objects.all():
                    data.append(i.toJSON())
            elif action == 'crear':

                ma = Marca()
                ma.nombre_marca = request.POST['nombre_marca']
                ma.descripcion_marca = request.POST['descripcion']         
                ma.usuario = User.objects.get(pk=1)
                ma.save()

                if request.FILES: 
                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(ma.pk)+"_"+imagen.name
                    ma.img_marca = imagen
                    ma.save()#Actualizamos la ruta de la imagen con la concatenacion del id recien creado
                
                data = {'tipo_accion': 'crear','correcto': True}

            elif action == 'editar':

                ma = Marca.objects.get(pk=request.POST['id'])
                ma.nombre_marca = request.POST['nombre_marca']
                ma.descripcion_marca = request.POST['descripcion']

                if request.FILES:
                    if ma.img_marca.url != "/media/img_defecto.jpg":
                        ma.img_marca.delete()

                    imagen = request.FILES.get("imagen") 
                    imagen.name = str(ma.pk)+"_"+imagen.name
                    ma.img_marca = imagen 

                ma.usuario = User.objects.get(pk=1)
                ma.save()
                
                data = {'tipo_accion': 'editar','correcto': True}

            elif action == 'eliminar':
                ma = Marca.objects.get(pk=request.POST['id'])
                if ma.img_marca.url != "/media/img_defecto.jpg":
                    ma.img_marca.delete()

                ma.delete()
                data = {'tipo_accion': 'eliminar','correcto': True}
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            data = {'tipo_accion': 'error','correcto': False, 'error': str(e)}

        return JsonResponse(data, safe=False)
    elif request.method == 'GET':
        print("Metodo normal")
        return render(request, 'marca/crear_marca.html',{'titulo':'Inicio','entidad':'Creacion de marcas'})