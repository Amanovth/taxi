# Generated by Django 5.0.1 on 2024-01-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0011_alter_rental_lon_b_alter_rental_point_b_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='lat_b',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Широта Б'),
        ),
    ]
