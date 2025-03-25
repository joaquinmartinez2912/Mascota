from rest_framework.viewsets import ModelViewSet
from api.serializers.Compras.compras_crud_serializers import CompraSerializer, CompraDetalleSerializer, DetallePorCompraSerializer
from compras.models import Compra, CompraDetalle

from django_filters.rest_framework import DjangoFilterBackend

class CompraViewSet(ModelViewSet):       
    queryset = Compra.objects.all()
    serializer_class = DetallePorCompraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ciclo','empresa','compra_detalle__insumo__categoria_id']

    def get_queryset(self):
        queryset = Compra.objects.all()

        ciclo = self.request.query_params.get('ciclo',None)
        empresa = self.request.query_params.get('empresa', None)
        categoria = self.request.query_params.get('categoria', None)
        
        if ciclo:
            queryset = queryset.filter(ciclo=ciclo)
        if empresa:
            queryset = queryset.filter(empresa=empresa)
        if categoria:
            queryset = queryset.filter(compra_detalle__insumo__categoria_id=categoria)

        return queryset

class CompraDetalleViewSet(ModelViewSet):
    queryset = CompraDetalle.objects.all()         
    serializer_class = CompraDetalleSerializer
    