from rest_framework.viewsets import ModelViewSet
from api.serializers.Establecimiento.estab_crud_serializers import CampoSerializer, LoteSerializer
from establecimiento.models import Campo, Lote

class CampoViewSet(ModelViewSet):
    queryset = Campo.objects.all()
    serializer_class = CampoSerializer

class LoteViewSet(ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer




