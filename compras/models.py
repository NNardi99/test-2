from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MinValueValidator
from datetime import date
from administrador.models import Producto, CustomUser, Proveedor

# # Create your models here.
class Compra(models.Model):
    codigo = models.AutoField(primary_key=True)
    comprador = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha = models.DateField(default=date.today)

    def delete(self, *args, **kwargs):
        for item in self.items.all():
            item.producto.stockAct-=item.cantidad
            item.producto.save()
        super(Compra, self).delete(*args, **kwargs)

class DetalleCompra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name_plural = "Detalle de Compras"
        verbose_name = "Detalle de Compra"

# Crear función para hacer override del save del model
    def save(self, *args, **kwargs):
        if not self.id:
            producto = Producto.objects.get(
                nombre=self.producto
            )
            producto.stockAct += self.cantidad
            producto.save()
        super(DetalleCompra, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        producto = Producto.objects.get(
            nombre=self.producto
        )
        producto.stockAct -= self.cantidad
        producto.save()
        super(DetalleCompra, self).delete(*args, **kwargs)