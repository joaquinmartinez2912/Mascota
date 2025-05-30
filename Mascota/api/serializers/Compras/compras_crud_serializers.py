from rest_framework import serializers
from compras.models import Compra, CompraDetalle
from api.serializers.Insumos.insumos_crud_serializers import InsumosSerializer

class CompraSerializer(serializers.ModelSerializer):   
    total_compra = serializers.ReadOnlyField()

    class Meta:
        model = Compra
        fields = ('id', 'fecha','ciclo', 'empresa', 'total_compra')

class CompraDetalleSerializer(serializers.ModelSerializer):
    compra = CompraSerializer()
    insumo = InsumosSerializer()
    total = serializers.ReadOnlyField()

    class Meta:
        model = CompraDetalle
        fields =('compra','insumo','precio','cantidad','total')

class CompraDetalleMinSerializer(serializers.ModelSerializer):
    insumo = InsumosSerializer()
    total = serializers.ReadOnlyField()

    class Meta:
        model = CompraDetalle
        fields =('insumo','precio','cantidad','total')

class DetallePorCompraSerializer(serializers.ModelSerializer):
    detalle = serializers.SerializerMethodField()

    class Meta:
        model = Compra
        fields = ('id', 'fecha','ciclo', 'empresa', 'total_compra','detalle')

    def get_detalle(self, obj):
        return CompraDetalleMinSerializer(obj.compra_detalle.all(),many=True).data
    

    