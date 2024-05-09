from turtle import mode
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre de las gafas")

    def __str__(self):
      return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre del Producto", db_index=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField( upload_to='imagenes/', verbose_name="Imagen", null=True, blank=True)
    descripcion = models.TextField(null=True)
    especial = models.BooleanField(default=False, verbose_name="Producto especial")
    disponible = models.BooleanField(default=False, verbose_name="Disponibilidad del producto")

    def __str__(self):
      return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete(using=using, keep_parents=keep_parents)