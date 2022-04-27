from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import model_to_dict

from distribuidora.settings.local import MEDIA_URL



class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=20, verbose_name="Nombre de la categoría", null=False, blank=False)
    descripcion_categoria = models.CharField(max_length=50,default="No",blank = True, null = True, verbose_name="Descripción")
    img_categoria = models.ImageField(upload_to='categorias_empresa/',
    verbose_name='Imagen', null=True, blank=True,default='img_defecto.jpg')
    fecha_registro = models.DateField(auto_now_add=True,blank=True,null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.pk,self.nombre_categoria)

    def toJSON(self):
        item = model_to_dict(self) #Convertimos todos los objetos en diccionarios
        item['img_categoria'] = self.img_categoria.url
        return item
