# Generated by Django 4.1.5 on 2023-04-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_supplier_request',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier_request',
            name='dt',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier_request',
            name='tm',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]