# Generated by Django 2.2 on 2020-08-19 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='tipoMaterial',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='tipoPersona',
        ),
    ]
