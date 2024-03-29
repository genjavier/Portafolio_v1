# Generated by Django 2.2.4 on 2019-09-16 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField(verbose_name='rut')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('correo', models.EmailField(max_length=255, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('fecha_modificacion', models.DateField(blank=True, null=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
            },
        ),
    ]
