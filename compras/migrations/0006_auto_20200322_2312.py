# Generated by Django 3.0.4 on 2020-03-23 02:12

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_remove_producto_estado'),
        ('compras', '0005_auto_20200322_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administrador.Marca'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='producto',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='marca', chained_model_field='marca', null=True, on_delete=django.db.models.deletion.PROTECT, to='administrador.Producto'),
        ),
    ]