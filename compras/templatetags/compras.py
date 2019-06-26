from django import template
import json
register = template.Library()

@register.simple_tag
def saludar(queryset):
    mapa = {}
    productos = []
    for compra in queryset.all():
        for detalle in compra.items.all():
            mapa[detalle.producto.nombre] =mapa.get(detalle.producto.nombre, 0) + detalle.cantidad
    print(mapa)
    return mapa