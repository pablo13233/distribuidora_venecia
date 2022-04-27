from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.db import models


# Create your models her

class Carrusel(models.Model):
    nombre_Carrusel = models.CharField(max_length=25, verbose_name="nombre de la imagen")
    descripcion_Carrusel = models.CharField(max_length=100,  blank=True, null= True, verbose_name="Descripcion de imagen")
    imagen_Carrusel = models.ImageField(upload_to = 'carrusel/', verbose_name='Image')
    estado_Carrusel = models.BooleanField(default=True, verbose_name="Estado")
    direccion_Carrusel = models.URLField(max_length = 200,  blank=True, null= True, verbose_name='Direccion de categoria de productos' )
    fecha_registro_Carrusel = models.DateField(auto_now_add=True, blank=True, null= True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.pk,self.nombre_Carrusel)
    
    def toJSON(self):
        item = model_to_dict(self) #Convertimos los objetos en diccionarios
        item['imagen_Carrusel'] = self.imagen_Carrusel.url
        return item
