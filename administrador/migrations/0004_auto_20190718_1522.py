# Generated by Django 2.2 on 2019-07-18 18:22

from django.db import migrations

def populate_riesgo(apps, schema_editor):
    Producto = apps.get_model('administrador', 'Producto')
    for producto in Producto.objects.all():
        producto.riesgo = 1
        producto.save()

class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_riesgo'),
    ]

    operations = [
        migrations.RunPython(populate_riesgo),
    ]