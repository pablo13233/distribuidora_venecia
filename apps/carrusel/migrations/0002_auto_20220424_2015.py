# Generated by Django 3.2.13 on 2022-04-25 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrusel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrusel',
            old_name='estado',
            new_name='estado_Carrusel',
        ),
        migrations.RenameField(
            model_name='carrusel',
            old_name='fecha_registro',
            new_name='fecha_registro_Carrusel',
        ),
        migrations.RenameField(
            model_name='carrusel',
            old_name='imagen',
            new_name='imagen_Carrusel',
        ),
        migrations.RenameField(
            model_name='carrusel',
            old_name='nombre',
            new_name='nombre_Carrusel',
        ),
        migrations.RemoveField(
            model_name='carrusel',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='carrusel',
            name='direccion',
        ),
        migrations.AddField(
            model_name='carrusel',
            name='descripcion_Carrusel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripcion de imagen'),
        ),
        migrations.AddField(
            model_name='carrusel',
            name='direccion_Carrusel',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion de categoria de productos'),
        ),
    ]
