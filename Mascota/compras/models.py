from django.db import models
from insumos.models import Insumo
from proveedor.models import Proveedor

# Create your models here.

class Compra(models.Model):
    fecha = models.DateField()
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT, related_name = 'compras',
null=False)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    ciclo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)

    @property
    def total(self):
        return self.cantidad * self.precio

