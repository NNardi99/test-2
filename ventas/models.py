from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MinValueValidator
from datetime import date
from administrador.models import Producto, CustomUser, Cliente

# # Create your models here.
class Venta(models.Model):
    codigo = models.AutoField(primary_key=True)
    vendedor = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateField(default=date.today)

    def delete(self, *args, **kwargs):
        for item in self.items.all():
            item.producto.stockAct+=item.cantidad
            item.producto.save()
        super(Venta, self).delete(*args, **kwargs)

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name_plural = "Detalle de Ventas"
        verbose_name = "Detalle de Venta"

# Crear función para hacer override del save del model
    def save(self, *args, **kwargs):
        if not self.id:
            producto = Producto.objects.get(
                nombre=self.producto
            )
            producto.stockAct -= self.cantidad
            producto.save()
        super(DetalleVenta, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        producto = Producto.objects.get(
            nombre=self.producto
        )
        producto.stockAct += self.cantidad
        producto.save()
        super(DetalleVenta, self).delete(*args, **kwargs)