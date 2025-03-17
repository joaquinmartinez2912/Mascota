from django.contrib import admin
from compras.models import Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'insumo', 'cantidad', 'precio', 'ciclo', 'empresa', 'total')
    readonly_fields = ('total',) 



