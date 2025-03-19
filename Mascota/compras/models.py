from django.db import models
from insumos.models import Insumo
from proveedor.models import Proveedor

# Create your models here.

class Compra(models.Model):
    fecha = models.DateField()
    ciclo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)

    @property
    def total_compra(self):
        return sum(detalle.total for detalle in self.compra_detalle.all() )

    def __str__(self):
        return self.ciclo

class CompraDetalle(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.PROTECT, related_name='compra_detalle')
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT, related_name = 'compras',
null=False)
    precio = models.FloatField(default=0)
    cantidad = models.FloatField(default=0)

    @property
    def total(self):
        return self.cantidad * self.precio
