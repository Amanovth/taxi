# Generated by Django 5.0.1 on 2024-01-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0009_alter_driver_number_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='lat',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='lon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]