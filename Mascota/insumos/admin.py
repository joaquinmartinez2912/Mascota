from django.contrib import admin
from insumos.models import Categoria, Insumo

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']
    search_fields = ['id','nombre']          

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo', 'cantidad', 'unidad_medida', 'proveedor', 'categoria']
    

