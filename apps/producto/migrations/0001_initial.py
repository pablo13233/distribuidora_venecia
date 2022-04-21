# Generated by Django 3.2.12 on 2022-04-21 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categoria', '0001_initial'),
        ('marca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=20, verbose_name='Nombre del producto')),
                ('descripcion_producto', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('img_producto', models.ImageField(blank=True, default='img_defecto.jpg', null=True, upload_to='productos_empresa/', verbose_name='Imagen')),
                ('fecha_registro', models.DateField(auto_now_add=True, null=True)),
                ('precio', models.FloatField(blank=True, default=0, null=True, verbose_name='Precio')),
                ('estado_producto', models.BooleanField(default=True, verbose_name='Estado')),
                ('modelo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Modelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria', verbose_name='Categoría')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marca.marca', verbose_name='Marca')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]