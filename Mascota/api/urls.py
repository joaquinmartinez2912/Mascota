from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.Insumos.insumos_crud_views import InsumosViewSet

router = DefaultRouter()
router.register(r'insumos', InsumosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
