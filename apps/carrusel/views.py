import re
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required #Manejo de permisos
from django.views.generic import(ListView,CreateView,TemplateView,UpdateView,DetailView,DeleteView)
from django.shortcuts import HttpResponse

from apps.carrusel.models import Carrusel



# Create your views here.

@login_required
def gestion_carrusel_ajax (request):
    if request.method == 'POST' and request.is_ajax():
        data = []
        try:
            action = request.POST['action']
            if action =='buscardatos':
                for i in Carrusel.objects.all():
                    data.append(i.toJSON())

                    #========================   Crear   =========================
            elif action =='crear':

                dato_Carrusel = Carrusel()
                dato_Carrusel.nombre_Carrusel = request.POST['nombre_Carrusel']
                dato_Carrusel.descripcion_Carrusel = request.POST['descripcion_Carrusel']
                dato_Carrusel.estado_Carrusel = request.POST['estado_Carrusel']
                dato_Carrusel.direccion_Carrusel = request.POST['direccion_Carrusel']


                dato_Carrusel.usuario = User.objects.get(pk=request.user.id)
                dato_Carrusel.save()

                if request.FILES:
                    imagen = request.FILES.get("imagen")
                    imagen.name = str(dato_Carrusel.pk)+"_"+imagen.name
                    dato_Carrusel.imagen_Carrusel =imagen
                    dato_Carrusel.save()#Actualizamos la ruta de la imagen con la concatenacion del id recien creado
                data = {'tipo_accion': 'crear', 'correcto': True}

                #========================   editar   =========================
            elif action == 'editar':

                dato_Carrusel = Carrusel.objects.get(pk=request.POST['id'])
                dato_Carrusel.nombre_Carrusel = request.POST['nombre_Carrusel']
                dato_Carrusel.descripcion_Carrusel = request.POST['descripcion_Carrusel']
                dato_Carrusel.estado_Carrusel = request.POST['estado_Carrusel']
                dato_Carrusel.direccion_Carrusel = request.POST['direccion_Carrusel']

                if request.FILES:
                    if dato_Carrusel.imagen_Carrusel.url != "/media/img_defecto.jpg":
                        dato_Carrusel.imagen_Carrusel.delete()

                    imagen = request.FILES.get("imagen")
                    imagen.name = str(dato_Carrusel.pk)+"_"+imagen.name
                    dato_Carrusel.imagen_Carrusel = imagen
                    
                dato_Carrusel.save()
                data = {'tipo_accion': 'editar', 'correcto': True}

                #========================   eliminar   =========================
            elif action =='eliminar':
                dato_Carrusel = Carrusel.objects.get(pk=request.POST['id'])
                if dato_Carrusel.imagen_Carrusel.url != "/media/img_defecto.jpg":
                    dato_Carrusel.imagen_Carrusel.delete()

                dato_Carrusel.delete()
                data = {'tipo_accion': 'eliminar', 'correcto': True}
            else:
                data['error'] = 'Ha ocurrido un error'
            


        except Exception as e:
            data['error'] = str(e)
            data = {'tipo_accion': 'error', 'correcto': False, 'error': str(e)}
        return JsonResponse(data,safe=False)
    elif request.method =="GET":
        return render(request, 'carrusel/gestion_carrusel.html')
    
