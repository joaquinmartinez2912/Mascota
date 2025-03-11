from rest_framework.viewsets import ModelViewSet
from api.serializers.Proveedores.proveedores_crud_serializers import ProveedorSerializer
from proveedor.models import Proveedor

class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer  

