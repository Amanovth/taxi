# Generated by Django 5.0.1 on 2024-01-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_rename_auto_tariff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Водитель', 'verbose_name_plural': 'Водители'},
        ),
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(default=1, max_length=55, verbose_name='Имя водителя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='number_auto',
            field=models.IntegerField(default=1, verbose_name='Регистрационный номер автомобиля'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='star',
            field=models.IntegerField(blank=True, default=1, verbose_name='Оценки водителя'),
            preserve_default=False,
        ),
    ]