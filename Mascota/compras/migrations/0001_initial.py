# Generated by Django 5.1.5 on 2025-03-19 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insumos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ciclo', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CompraDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(default=0)),
                ('cantidad', models.FloatField(default=0)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compra_detalle', to='compras.compra')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to='insumos.insumo')),
            ],
        ),
    ]
