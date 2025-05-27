from django.contrib import admin
from Ordenes.models import Ordenes, OrdenesDetalle, OrdenesLote

# Register your models here.

@admin.register(Ordenes)
class OrdenesAdmin(admin.ModelAdmin):
    list_display = ['fecha']

@admin.register(OrdenesDetalle)
class OrdenesDetalleAdmin(admin.ModelAdmin):
    list_display = ['orden','insumo','cantidad']
    search_fields = ['orden__id', 'insumo__nombre']

@admin.register(OrdenesLote)
class OrdenesLoteAdmin(admin.ModelAdmin):
    list_display = ['orden', 'lote']
    search_fields = ['orden__id', 'lote__id']

