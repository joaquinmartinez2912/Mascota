from django.contrib import admin
from establecimiento.models import Campo, Lote

# Register your models here.

@admin.site.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion']
    search_fields = ['nombre', 'direccion']

@admin.site.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'superficie', 'campo']
    search_fields = ['nombre', 'campo']