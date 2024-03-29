from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from . import choices


class Driver(models.Model):
    # Driver
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    status = models.IntegerField(_('Статус'), default=2, choices=choices.STATUS_CHOICES)
    city = models.CharField(_('Город'), choices=choices.CITY_CHOICE)
    lat = models.CharField('Широта', null=True, blank=True, max_length=500)
    lon = models.CharField('Долгота', null=True, blank=True, max_length=500)
    # Job
    driver_photo = models.ImageField(_('Фото водителя'), upload_to='driver_photos', default='driver_photos/driver.png')
    car_tariff = models.OneToOneField('Tariff', on_delete=models.CASCADE, verbose_name=_('Тариф'))
    car_brand = models.CharField(_('Марка машины'), max_length=255)
    car_model = models.CharField(_('Модель автомобиля'), max_length=255)
    car_color = models.CharField(_('Цвет автомобиля'), max_length=255)
    number_auto = models.CharField(_('Регистрационный номер автомобиля'), max_length=20)
    # Star
    total_star = models.IntegerField(default=0, editable=False)
    users_star = models.IntegerField(default=0, editable=False)
    star = models.DecimalField(_('Рейтинг водителя'), max_digits=5, decimal_places=2, default=0.00)
    # Driver License
    lisence_country = models.CharField(_('Страна получения ВУ'), choices=choices.COUNTIES_CHOICE, max_length=200, blank=True, null=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, blank=True, null=True)
    first_name = models.CharField(_('Имя'), max_length=255, blank=True, null=True)
    lisence_number = models.CharField(_('Номер ВУ'), max_length=255, blank=True, null=True)
    issue_date = models.DateField(_('Когда выдано'), blank=True, null=True)


    def __str__(self):
        return f"{self.car_color} {self.car_brand} {self.car_model}, {self.user.first_name} {self.user.last_name}"


    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

class Tariff(models.Model):
    name = models.CharField(_('Тариф'), max_length=255)
    car_icon = models.ImageField(_('Изображение автомобиля'), upload_to='car_icons')
    get_into = models.IntegerField(_('Посадка в авто'))
    free_waiting = models.IntegerField(_('Бесплатное ожидание'), help_text='В минутах')
    paid_waiting = models.IntegerField(_('Платное ожидание'), help_text='сом/мин')
    around_city_km = models.FloatField(_('Стоимость поездки по городу'), help_text='сом/км')
    around_city_min = models.FloatField(_('Стоимость поездки по городу'), help_text='сом/мин')
    out_of_city_km = models.FloatField(_('Стоимость поездки за пределами города'), help_text='сом/км')
    out_of_city_min = models.FloatField(_('Стоимость поездки за пределами города'), help_text='сом/мин')
    pet_transportation = models.IntegerField(_('Перевозка домашнего животного'), help_text='не более')
    only_by_text = models.IntegerField(_('Общаюсь только текстом'), help_text='не более')
    air_conditioner = models.IntegerField(_('Кондиционер'), help_text='не более')
    with_wheelchair = models.IntegerField(_('Буду с инвалидным креслом'), help_text='не более')
    do_not_speak_but_hear = models.IntegerField(_('Не говорю, но слышу'), help_text='не более')
    help_find_car = models.IntegerField(_('Помогите найти машину'), help_text='не более')
    waiting_on_the_way = models.IntegerField(_('Ожидание в пути'), help_text='не более x сом/мин')

    def __str__(self):
        return f'Тариф - {self.name}'

    class Meta:
        verbose_name = _('Тариф')
        verbose_name_plural = _('Тарифы')

