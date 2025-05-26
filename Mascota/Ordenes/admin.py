from django.contrib import admin
from Ordenes.models import Ordenes

# Register your models here.

@admin.register(Ordenes)
class OrdenesAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'insumo', 'lote', 'cantidad']
    search_fields = ['insumo__nombre', 'lote__nombre']
