# Generated by Django 4.1.5 on 2023-04-17 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0003_tbl_material_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=200, null=True)),
                ('material_Durability', models.CharField(max_length=200, null=True)),
                ('material_density', models.CharField(max_length=100, null=True)),
                ('material_Water_absorption', models.CharField(max_length=200, null=True)),
                ('strength', models.CharField(max_length=100, null=True)),
                ('Hardness', models.CharField(max_length=100, null=True)),
                ('Elasticity', models.CharField(max_length=200, null=True)),
                ('dt', models.DateField(auto_now_add=True, null=True)),
                ('tm', models.TimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='constructapp.tbl_material_category')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='constructapp.tbl_supplier_request')),
            ],
        ),
    ]