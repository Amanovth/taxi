# Generated by Django 5.0.1 on 2024-01-27 06:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_alter_rental_status_alter_rental_time_end_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rentals_as_driver', to=settings.AUTH_USER_MODEL, verbose_name='Водитель'),
        ),
    ]
