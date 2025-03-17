from rest_framework import serializers
from compras.models import Compra
from api.serializers.Insumos.insumos_crud_serializers import InsumosSerializer

class CompraSerializer(serializers.ModelSerializer):   
    insumo = InsumosSerializer()
    total = serializers.ReadOnlyField()

    class Meta:
        model = Compra
        fields = ('id', 'fecha', 'insumo', 'cantidad', 'precio', 'ciclo', 'empresa', 'total')