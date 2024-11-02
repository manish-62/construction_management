# Generated by Django 4.1.5 on 2023-04-17 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0007_tbl_uploaded_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_design_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_type', models.CharField(max_length=100, null=True)),
                ('sq_ft', models.CharField(max_length=100, null=True)),
                ('bays', models.CharField(max_length=100, null=True)),
                ('beds', models.CharField(max_length=100, null=True)),
                ('baths', models.CharField(max_length=100, null=True)),
                ('width', models.CharField(max_length=100, null=True)),
                ('depth', models.CharField(max_length=100, null=True)),
                ('Image', models.ImageField(null=True, upload_to='media')),
                ('dt', models.DateField(auto_now_add=True, null=True)),
                ('tm', models.TimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='constructapp.tbl_registration')),
            ],
        ),
    ]