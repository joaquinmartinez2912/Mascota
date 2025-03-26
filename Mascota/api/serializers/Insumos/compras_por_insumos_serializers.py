from rest_framework import serializers
from insumos.models import Insumo
from compras.models import Compra, CompraDetalle

class CompraInsumoMinSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = CompraDetalle
        fields =('precio','cantidad','total')

class DetallePorCompraSerializer(serializers.ModelSerializer):
    detalle = serializers.SerializerMethodField()

    class Meta:
        model = Compra
        fields = ('fecha','ciclo','detalle')

    def get_detalle(self, obj):
            insumo_id = self.context.get('insumo_id') 
            detalles_filtrados = obj.compra_detalle.filter(insumo_id=insumo_id) 
            return CompraInsumoMinSerializer(detalles_filtrados, many=True).data  

class DetallePorInsumoSerializer(serializers.ModelSerializer):
    detalle_compra = serializers.SerializerMethodField()

    class Meta:
        model = Insumo
        fields = ('nombre','proveedor','detalle_compra')

    def get_detalle_compra(self, obj):
        compras = Compra.objects.filter(compra_detalle__insumo=obj).distinct()
        return DetallePorCompraSerializer(compras, many=True, context={'insumo_id': obj.id}).data
    