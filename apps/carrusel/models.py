from io import UnsupportedOperation
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models

# Create your models her

class Carrusel(models.Model):
    nombre = models.CharField(max_length=25, verbose_name="nombre de la imagen")
    descripcion = models.CharField(max_length=100, verbose_name="Descripcion de imagen")
    imagen = models.ImageField(upload_to = 'carruse/', verbose_name='Image')
    estado = models.BooleanField(default=True, verbose_name="Estado")
    direccion = models.URLField(max_length = 200, verbose_name='Direccion de categoria de productos' )
    fecha_registro = models.DateField(auto_now_add=True, blank=True, null= True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.pk,self.nombre)
