# Generated by Django 5.0.1 on 2024-02-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0017_alter_driver_total_star_alter_driver_users_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='star',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Рейтинг водителя'),
        ),
    ]
