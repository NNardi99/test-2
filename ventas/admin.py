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
    ]

    inlines = [
        DetalleVentaInline,
    ]

    form = VentasForm

    list_display = ('codigo', 'vendedor', 'cliente', 'fecha')
    search_fields = ('vendedor', 'cliente', 'fecha')
    list_filter = ('vendedor', 'cliente', 'fecha')
    ordering = ('codigo',)
    change_list_template = 'admin/change_list_graph_sell.html'

admin.site.register(Venta, VentaAdmin)