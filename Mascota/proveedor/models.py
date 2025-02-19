from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    cuit = models.CharField(max_length=11,
validators=[MinLengthValidator(11, message="Deben ser 11 caracteres"),
MaxLengthValidator(11, message="Deben ser 11 caracteres")])
             
    def __str__(self):    
        return self.nombre 

    class Meta:
        verbose_name_plural = "Proveedores"