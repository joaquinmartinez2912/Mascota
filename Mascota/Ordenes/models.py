from django.db import models
from insumos.models import Insumo
from establecimiento.models import Lote

# Create your models here.

class Ordenes(models.Model):
    fecha = models.DateField()
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name='ordenes', null=False)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name='ordenes', null=False)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Orden {self.id} - {self.fecha} - {self.insumo.nombre}"

