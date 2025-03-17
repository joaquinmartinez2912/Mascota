from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.Insumos.insumos_crud_views import InsumosViewSet
from api.views.Establecimientos.estab_crud_views import CampoViewSet, LoteViewSet
from api.views.Proveedores.proveedores_crud_views import ProveedorViewSet
from api.views.Compras.compras_crud_views import CompraViewSet

router = DefaultRouter()
router.register(r'insumos', InsumosViewSet)
router.register(r'campos', CampoViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'compras', CompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
