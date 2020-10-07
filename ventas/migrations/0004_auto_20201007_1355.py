# Generated by Django 3.0.4 on 2020-10-07 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_remove_producto_estado'),
        ('ventas', '0003_auto_20200323_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleventa',
            options={'verbose_name_plural': 'Detalle de Ventas'},
        ),
        migrations.RemoveField(
            model_name='venta',
            name='estado',
        ),
        migrations.AlterUniqueTogether(
            name='detalleventa',
            unique_together={('venta', 'producto')},
        ),
    ]