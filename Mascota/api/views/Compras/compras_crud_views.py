from rest_framework.viewsets import ModelViewSet
from api.serializers.Compras.compras_crud_serializers import CompraSerializer
from compras.models import Compra

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()         
    serializer_class = CompraSerializer

    