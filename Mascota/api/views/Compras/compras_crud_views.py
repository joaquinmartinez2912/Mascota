from rest_framework.viewsets import ModelViewSet
from api.serializers.Compras.compras_crud_serializers import CompraSerializer, CompraDetalleSerializer
from compras.models import Compra, CompraDetalle

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()         
    serializer_class = CompraSerializer

class CompraDetalleViewSet(ModelViewSet):
    queryset = CompraDetalle.objects.all()         
    serializer_class = CompraDetalleSerializer
    