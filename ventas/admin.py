from django.contrib import admin
from .models import DetalleVenta, Venta

from ventas.forms import MyForm, VentasForm

# Register your models here.

class DetalleVentaInline(admin.StackedInline):
    model = DetalleVenta
    extra = 1
    form = MyForm

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
    ordering = ('codigo',)

admin.site.register(Venta, VentaAdmin)