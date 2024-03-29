# Generated by Django 4.2.8 on 2023-12-16 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariff', models.CharField(max_length=255, verbose_name='Тариф')),
                ('car_icon', models.ImageField(upload_to='car_icons', verbose_name='Изображение автомобиля')),
                ('get_into', models.IntegerField(verbose_name='Посадка в авто')),
                ('free_waiting', models.IntegerField(help_text='В минутах', verbose_name='Бесплатное ожидание')),
                ('paid_waiting', models.IntegerField(help_text='сом/мин', verbose_name='Платное ожидание')),
                ('around_city_km', models.FloatField(help_text='сом/км', verbose_name='Стоимость поездки по городу')),
                ('around_city_min', models.FloatField(help_text='сом/мин', verbose_name='Стоимость поездки по городу')),
                ('out_of_city_km', models.FloatField(help_text='сом/км', verbose_name='Стоимость поездки за пределами города')),
                ('out_of_city_min', models.FloatField(help_text='сом/мин', verbose_name='Стоимость поездки за пределами города')),
                ('pet_transportation', models.IntegerField(help_text='не более', verbose_name='Перевозка домашнего животного')),
                ('only_by_text', models.IntegerField(help_text='не более', verbose_name='Общаюсь только текстом')),
                ('air_conditioner', models.IntegerField(help_text='не более', verbose_name='Кондиционер')),
                ('with_wheelchair', models.IntegerField(help_text='не более', verbose_name='Буду с инвалидным креслом')),
                ('do_not_speak_but_hear', models.IntegerField(help_text='не более', verbose_name='Не говорю, но слышу')),
                ('help_find_car', models.IntegerField(help_text='не более', verbose_name='Помогите найти машину')),
                ('waiting_on_the_way', models.IntegerField(help_text='не более x сом/мин', verbose_name='Ожидание в пути')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=255, verbose_name='Марка машины')),
                ('car_model', models.CharField(max_length=255, verbose_name='Модель автомобиля')),
                ('car_color', models.CharField(max_length=255, verbose_name='Цвет автомобиля')),
                ('driver_photo', models.ImageField(default='driver_photos/driver.png', upload_to='driver_photos', verbose_name='Фото водителя')),
                ('car_tariff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drivers.auto', verbose_name='Тариф')),
            ],
        ),
    ]
