# Generated by Django 3.1.1 on 2020-09-12 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('clave', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.salon')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id_clase', models.IntegerField(primary_key=True, serialize=False)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.salon')),
            ],
        ),
    ]