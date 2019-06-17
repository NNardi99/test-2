from django.contrib import admin
from .models import DetalleVenta, Venta

from ventas.forms import MyForm

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

# class DetalleVentaAdmin(admin.ModelAdmin):
#     form = MyForm

admin.site.register(Venta, VentaAdmin)
# admin.site.register(DetalleVenta, DetalleVentaAdmin)