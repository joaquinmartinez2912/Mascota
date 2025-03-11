from rest_framework import serializers
from proveedor.models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'nombre', 'cuit')

    