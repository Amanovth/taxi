from django.db import models
# from django_2gis_maps import fields as map_fields
# from django_2gis_maps.mixins import DoubleGisMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# from src.drivers.models import Driver


# class Call(models.Model):
#     PAYMENT_CHOICES = (("1", "Наличные"), ("2", "С картой"))
#     passenger = models.ForeignKey(get_user_model(), verbose_name=_("Пассажир"), on_delete=models.CASCADE)
#     poit_a = models.CharField(_("Точка А"), max_length=255)
#     poit_b = models.CharField(_("Точка B"), max_length=255)
#     total_cost = models.IntegerField(_("Общая стоимость"))
#     payment_type = models.CharField(_("Тип оплаты"), choices=PAYMENT_CHOICES, max_length=8)

#     class Meta:
#         verbose_name = _("Вызов")
#         verbose_name_plural = _("Вызовы")

# class AcceptCall(models.Model):
#     call = models.ForeignKey(Call, on_delete=models.CASCADE)
#     driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = 'Принятый заказ'
#         verbose_name_plural = 'Принятые заказы'
    

class Rental(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'Ожидание'),
        ('accept', 'Принято'),
        ('ride', 'Поехали'),
        ('done', 'Доехали'),
        ('cancel', 'Отмена'),
    )
    PAYMENT_CHOICES = (
        ("1", "Наличные"), 
        ("2", "С картой")
    )
    
    passenger = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Пассажир"),
        on_delete=models.CASCADE,
        related_name="rentals_as_passenger"
    )

    driver = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Водитель"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="rentals_as_driver"
    )
    poit_a = models.CharField(_("Точка А"), max_length=255)
    poit_b = models.CharField(_("Точка B"), max_length=255)
    time_start = models.DateTimeField(_("Время начала"), blank=True, null=True)
    time_end = models.DateTimeField(_("Время окончания"), blank=True, null=True)
    total_cost = models.IntegerField(_("Общая стоимость"))
    payment_type = models.CharField(_("Тип оплаты"), choices=PAYMENT_CHOICES, max_length=8)
    route = models.ImageField(_("Маршрут поездки"), upload_to="routes/%Y/%m/%d/", blank=True)
    status = models.CharField(_('Статус'), choices=STATUS_CHOICES, max_length=100, default='waiting')

    def __str__(self):
        return f"{self.driver} {self.passenger}"

    class Meta:
        verbose_name = _("Поездка")
        verbose_name_plural = _("Поездки")
