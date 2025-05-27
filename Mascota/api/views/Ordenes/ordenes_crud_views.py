from rest_framework.viewsets import ModelViewSet
from api.serializers.Ordenes.ordenes_crud_serializers import OrdenesSerializer, OrdenesDetalleSerializer, OrdenesLoteSerializer
from insumos.models import Insumo
from Ordenes.models import Ordenes, OrdenesDetalle, OrdenesLote

class OrdenesViewSet(ModelViewSet):
    queryset = Ordenes.objects.all()
    serializer_class = OrdenesSerializer

class OrdenesDetalleViewSet(ModelViewSet):
    queryset = OrdenesDetalle.objects.all()
    serializer_class = OrdenesDetalleSerializer

class OrdenesLoteViewSet(ModelViewSet):
    queryset = OrdenesLote.objects.all()
    serializer_class = OrdenesLoteSerializer


    
