from django.contrib import admin
from .models import DetalleVenta, Venta

from ventas.forms import MyForm, VentasForm

# Register your models here.

class DetalleVentaInline(admin.StackedInline):
    model = DetalleVenta
    extra = 1
    form = MyForm
    
    # The inlines can't be changed or deleted
    def has_change_permission(self, request, obj=None):
        return False
    # def has_delete_permission(self, request, obj=None):
    #     return False

class VentaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fecha de Venta', {'fields': ['fecha']}),
        ('Vendedor', {'fields': ['vendedor']}),
        ('Cliente', {'fields': ['cliente']}),
        ('Estado', {'fields': ['estado']}),
    ]

    inlines = [
        DetalleVentaInline,
    ]

    form = VentasForm

    list_display = ('codigo', 'vendedor', 'cliente', 'fecha', 'estado')
    search_fields = ('vendedor_id__first_name', 'vendedor_id__last_name', 'cliente_id__razon')
    list_filter = ('vendedor', 'cliente', 'fecha', 'estado')
    ordering = ('codigo',)
    change_list_template = 'admin/change_list_graph_sell.html'

admin.site.register(Venta, VentaAdmin)