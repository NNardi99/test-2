from django.contrib import admin
from .models import DetalleCompra, Compra

from compras.forms import MyForm, ComprasForm

# Register your models here.

class DetalleCompraInline(admin.StackedInline):
    model = DetalleCompra
    extra = 1
    form = MyForm
    
    # The inlines can't be changed or deleted
    def has_change_permission(self, request, obj=None):
        return False
    # def has_delete_permission(self, request, obj=None):
    #     return False

class CompraAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fecha de Compra', {'fields': ['fecha']}),
        ('Comprador', {'fields': ['comprador']}),
        ('Proveedor', {'fields': ['proveedor']}),
    ]

    inlines = [
        DetalleCompraInline,
    ]

    form = ComprasForm

    list_display = ('codigo', 'comprador', 'proveedor', 'fecha')
    search_fields = ('comprador', 'proveedor', 'fecha')
    list_filter = ('comprador', 'proveedor', 'fecha')
    ordering = ('codigo',)

admin.site.register(Compra, CompraAdmin)