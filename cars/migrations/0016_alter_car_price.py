# Generated by Django 5.1 on 2024-09-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_rename_plate_numer_car_plate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço'),
        ),
    ]
