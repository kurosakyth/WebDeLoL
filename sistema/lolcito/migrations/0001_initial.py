# Generated by Django 3.2.8 on 2022-04-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fondo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='images/', verbose_name='Imagen')),
            ],
        ),
    ]
