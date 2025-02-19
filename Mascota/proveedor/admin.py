from django.contrib import admin
from proveedor.models import Proveedor

# Register your models here.

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cuit']
    search_fields = ['nombre', 'cuit']