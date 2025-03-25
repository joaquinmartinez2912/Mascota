from rest_framework import serializers
from insumos.models import Insumo, Categoria
from api.serializers.Proveedores.proveedores_crud_serializers import ProveedorSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')
    

class InsumosSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    proveedor = ProveedorSerializer()

    class Meta:
        model = Insumo
        fields = ('id', 'nombre', 'codigo', 'cantidad', 'unidad_medida', 'proveedor', 'categoria')