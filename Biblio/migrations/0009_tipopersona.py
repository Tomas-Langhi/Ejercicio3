# Generated by Django 2.2 on 2020-08-20 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0008_tipomaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alumno', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblio.Alumno')),
                ('Profesor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblio.Profesor')),
            ],
        ),
    ]
