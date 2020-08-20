# Generated by Django 2.2 on 2020-08-19 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0004_remove_material_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='material',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='persona',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblio.Alumno'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblio.Libro'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblio.Profesor'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='revista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblio.Revista'),
        ),
    ]
