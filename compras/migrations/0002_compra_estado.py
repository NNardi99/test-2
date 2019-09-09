# Generated by Django 2.2 on 2019-09-09 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='estado',
            field=models.CharField(choices=[('1', 'Pendiente'), ('2', 'Vendido'), ('3', 'Cancelado')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]