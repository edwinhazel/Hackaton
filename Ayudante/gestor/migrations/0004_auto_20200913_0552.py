# Generated by Django 3.1.1 on 2020-09-13 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0003_auto_20200913_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='name',
            new_name='nombre',
        ),
    ]
