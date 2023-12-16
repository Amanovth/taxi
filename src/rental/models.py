from django.db import models
# from django_2gis_maps import fields as map_fields
# from django_2gis_maps.mixins import DoubleGisMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from src.drivers.models import Driver


class Rental(models.Model):
    PAYMENT_CHOICES = (
        ('Наличные', 'Наличные'),
        ('С картой', 'С картой')
    )
    passenger = models.OneToOneField(get_user_model(), verbose_name=_('Пассажир'), on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver, verbose_name=_('Водитель'), on_delete=models.CASCADE)
    poit_a = models.CharField(_('Точка А'), max_length=255)
    poit_b = models.CharField(_('Точка B'), max_length=255)
    time_start = models.DateTimeField(_('Время начала'))
    time_end = models.DateTimeField(_('Время окончания'))
    total_cost = models.IntegerField(_('Общая стоимость'))
    payment_type = models.CharField(_('Тип оплаты'), choices=PAYMENT_CHOICES, max_length=8)
    route = models.ImageField(_('Маршрут поездки'), upload_to='routes/%Y/%m/%d/')

    def __str__(self):
        return self.driver, self.passenger

    class Meta:
        verbose_name = _('Поездка')
        verbose_name_plural = _('Поездки')
