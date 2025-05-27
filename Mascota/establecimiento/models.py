from django.db import models

# Create your models here.

class Campo(models.Model):
    nombre = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Lote(models.Model):
    nombre = models.CharField(max_length=50)
    superficie = models.FloatField()
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, related_name = 'campos', null=False)

    def __str__(self):
        return self.nombre
