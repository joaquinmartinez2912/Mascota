from django.contrib import admin
from establecimiento.models import Campo, Lote

# Register your models here.

@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'localidad']
    search_fields = ['nombre', 'localidad']

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'superficie', 'campo']
    search_fields = ['nombre', 'campo']