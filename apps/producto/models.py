from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from apps.categoria.models import Categoria
from apps.marca.models import Marca

from distribuidora.settings.local import MEDIA_URL




class Producto(models.Model):
    nombre_producto = models.CharField(max_length=20, verbose_name="Nombre del producto")
    descripcion_producto = models.CharField(max_length=200, blank = True, null = True, verbose_name="Descripción")
    img_producto = models.ImageField(upload_to='productos_empresa/',verbose_name='Imagen', 
    null=True, blank=True,default='img_defecto.jpg')
    fecha_registro = models.DateField(auto_now_add=True,blank=True,null=True)
    precio = models.FloatField(default=0,blank = True, null = True, verbose_name="Precio")
    estado_producto = models.BooleanField(default = True, verbose_name="Estado")
    modelo = models.CharField(max_length=200,blank=True,null=True, verbose_name="Modelo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca",blank=True,null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.pk,self.nombre_producto)

    def toJSON(self):
        item = model_to_dict(self) #Convertimos todos los objetos en diccionarios
        item['img_producto'] = self.img_producto.url
        item['categoria'] = {'id': self.categoria.id, 'nombre': self.categoria.nombre_categoria}
        if self.marca == None:
            item['marca'] = {'id': 0, 'nombre': 'No registrado'}
        else:
            item['marca'] = {'id': self.marca.id, 'nombre': self.marca.nombre_marca}
        return item