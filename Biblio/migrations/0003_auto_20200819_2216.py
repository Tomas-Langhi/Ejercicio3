# Generated by Django 2.2 on 2020-08-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblio', '0002_auto_20200819_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]