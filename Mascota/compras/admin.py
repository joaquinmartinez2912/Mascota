from django.contrib import admin
from compras.models import Compra, CompraDetalle

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'ciclo', 'empresa', 'total_compra')
    readonly_fields = ('total_compra',) 


@admin.register(CompraDetalle)
class CompraDetalleAdmin(admin.ModelAdmin):
    list_display = ('id','compra','insumo','precio','cantidad','total')
    readonly_fields = ('total',)
