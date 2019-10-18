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
        ('Estado', {'fields': ['estado']}),
    ]

    inlines = [
        DetalleCompraInline,
    ]

    form = ComprasForm

    list_display = ('codigo', 'comprador', 'proveedor', 'fecha', 'estado')
    search_fields = ('comprador_id__first_name', 'comprador_id__last_name', 'proveedor_id__razon')
    list_filter = ('comprador', 'proveedor', 'fecha', 'estado')
    ordering = ('codigo',)
    change_list_template = 'admin/change_list_graph_buy.html'

admin.site.register(Compra, CompraAdmin)