# Generated by Django 2.2 on 2020-08-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0011_material_portada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='portada',
        ),
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.CharField(choices=[('IN', 'En biblioteca'), ('BW', 'Prestado'), ('RQ', 'Pedido'), ('RV', 'Reservado')], default='En biblioteca', max_length=2),
        ),
    ]
