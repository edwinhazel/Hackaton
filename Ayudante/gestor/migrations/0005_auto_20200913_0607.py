# Generated by Django 3.1.1 on 2020-09-13 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0004_auto_20200913_0552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clase',
            old_name='clase',
            new_name='num_clase',
        ),
    ]