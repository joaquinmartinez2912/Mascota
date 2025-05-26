from rest_framework.viewsets import ModelViewSet
from api.serializers.Ordenes.ordenes_crud_serializers import OrdenesSerializer
from insumos.models import Insumo
from Ordenes.models import Ordenes

class OrdenesViewSet(ModelViewSet):
    queryset = Ordenes.objects.all()
    serializer_class = OrdenesSerializer
    