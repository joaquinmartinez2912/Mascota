from rest_framework import serializers
from Ordenes.models import Ordenes, OrdenesDetalle, OrdenesLote

class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ('id', 'fecha')

class OrdenesDetalleSerializer(serializers.ModelSerializer):
    orden = OrdenesSerializer()

    class Meta:
        model = OrdenesDetalle
        fields = ('orden', 'insumo', 'cantidad')

class OrdenesLoteSerializer(serializers.ModelSerializer):
    orden = OrdenesSerializer()

    class Meta:
        model = OrdenesLote
        fields = ('orden', 'lote')

