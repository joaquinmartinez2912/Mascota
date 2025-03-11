from rest_framework import serializers
from establecimiento.models import Campo, Lote

class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo  
        fields = ('id', 'nombre', 'localidad')

class LoteSerializer(serializers.ModelSerializer):
    campo = CampoSerializer()

    class Meta:
        model = Lote
        fields = ('id', 'nombre', 'superficie', 'campo')