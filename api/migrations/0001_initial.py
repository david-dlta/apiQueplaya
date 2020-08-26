# Generated by Django 3.1 on 2020-08-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
                ('CODIGO', models.CharField(max_length=15)),
                ('LOCALIDAD', models.CharField(max_length=50)),
                ('DESCRIPCION1', models.CharField(max_length=500)),
                ('FECHA_ALTA', models.DateTimeField(auto_now_add=True)),
                ('FECHA_BAJA', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
