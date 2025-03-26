from rest_framework.viewsets import ReadOnlyModelViewSet
from api.serializers.Insumos.compras_por_insumos_serializers import DetallePorInsumoSerializer
from insumos.models import Insumo

class ComprasPorInsumoView(ReadOnlyModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = DetallePorInsumoSerializer

    def get_queryset(self):
        insumo_id = self.kwargs.get('insumo_id')
        if insumo_id:
            return Insumo.objects.filter(id=insumo_id)
        return Insumo.objects.none()
