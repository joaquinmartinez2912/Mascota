from rest_framework.viewsets import ModelViewSet
from api.serializers.Insumos.insumos_crud_serializers import InsumosSerializer
from insumos.models import Insumo

class InsumosViewSet(ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumosSerializer
    