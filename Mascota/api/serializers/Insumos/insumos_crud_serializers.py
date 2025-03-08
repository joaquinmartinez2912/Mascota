from rest_framework import serializers
from insumos.models import Insumo, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')
    

class InsumosSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Insumo
        fields = ('id', 'nombre', 'codigo', 'cantidad', 'unidad_medida', 'proveedor', 'categoria')