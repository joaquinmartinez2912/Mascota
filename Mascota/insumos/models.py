from django.db import models
from proveedor.models import Proveedor

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Insumo(models.Model):
    nombre = models.CharField(max_length=50)    
    codigo = models.CharField(max_length=50)
    cantidad = models.IntegerField()    
    unidad_medida = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, related_name = 'insumos',
null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name = 'insumos',
null=False)

    def __str__(self):
        return f"{self.nombre} ({self.id})"