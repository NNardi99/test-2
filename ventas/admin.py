from django.contrib import admin
from .models import DetalleVenta, Venta

# Register your models here.

class DetalleVentaInline(admin.StackedInline):
    model = DetalleVenta

class VentaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fecha de Venta', {'fields': ['fecha']}),
        ('Vendedor', {'fields': ['vendedor']}),
        ('Cliente', {'fields': ['cliente']}),
    ]

    inlines = [
        DetalleVentaInline,
    ]

admin.site.register(Venta, VentaAdmin)