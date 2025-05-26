from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.Insumos.insumos_crud_views import InsumosViewSet
from api.views.Establecimientos.estab_crud_views import CampoViewSet, LoteViewSet
from api.views.Proveedores.proveedores_crud_views import ProveedorViewSet
from api.views.Compras.compras_crud_views import CompraViewSet, CompraDetalleViewSet
from api.views.Insumos.compras_por_insumo_views import ComprasPorInsumoView
from api.views.Ordenes.ordenes_crud_views import OrdenesViewSet

router = DefaultRouter()
router.register(r'insumos', InsumosViewSet)
router.register(r'campos', CampoViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'compras_detalle', CompraDetalleViewSet)
router.register(r'ordenes', OrdenesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('compras_por_insumo/<int:insumo_id>/', ComprasPorInsumoView.as_view({'get': 'list'}), name='compras_por_insumo'),
]
