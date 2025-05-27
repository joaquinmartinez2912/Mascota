from django.db import models
from insumos.models import Insumo
from establecimiento.models import Lote

# Create your models here.

class Ordenes(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return f"Orden {self.id} - {self.fecha}"
    
class OrdenesDetalle(models.Model):
    orden = models.ForeignKey(Ordenes, on_delete=models.CASCADE, related_name='ordenes_detalle')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name='ordenes_detalle', null=False)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle {self.id} - Orden {self.orden.id} - Insumo {self.insumo.nombre}"

class OrdenesLote(models.Model):
    orden = models.ForeignKey(Ordenes, on_delete=models.CASCADE, related_name='ordenes_lote')
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='ordenes_lote', null=False)

    def __str__(self):
        return f"Lote {self.lote.id} - Orden {self.orden.id}"

