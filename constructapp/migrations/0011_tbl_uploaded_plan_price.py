# Generated by Django 4.1.5 on 2023-04-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructapp', '0010_final_cost_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_uploaded_plan',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
