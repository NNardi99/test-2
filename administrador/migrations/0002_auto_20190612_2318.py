# Generated by Django 2.2 on 2019-06-13 02:18

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='localidad',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='provincia', chained_model_field='provincia', null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Localidad'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Provincia'),
        ),
    ]
