# Generated by Django 5.1 on 2024-09-04 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_car_last_qualification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='creation_date',
            new_name='creation_date_time',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='last_modified',
            new_name='modified_date_time',
        ),
    ]
