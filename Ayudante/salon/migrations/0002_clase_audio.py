# Generated by Django 3.1.1 on 2020-09-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='audio',
            field=models.FileField(null=True, upload_to='audios/'),
        ),
    ]
