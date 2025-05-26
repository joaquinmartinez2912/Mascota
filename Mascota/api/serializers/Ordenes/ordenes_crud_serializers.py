from rest_framework import serializers
from Ordenes.models import Ordenes

class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ('id', 'fecha', 'insumo', 'lote', 'cantidad')

    