from random import randint
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("customer", _("Клиент")),
        ("driver", _("Таксист"))
    )
    username = None
    
    phone = models.CharField(_('Телефон номер'), unique=True, max_length=12)
    user_type = models.CharField(_('Статус'), choices=USER_TYPE_CHOICES, default="customer")
    code = models.IntegerField(_('Код активации'), null=True, blank=True)
    activated = models.BooleanField(_('Активировано'), default=False)

    # Bank card
    card_num = models.IntegerField(_('Номер карты'), null=True, blank=True)
    valid = models.DateField(_('Действует до'), null=True, blank=True)
    cvv = models.IntegerField(_('CVV'), null=True, blank=True)

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.code = int(randint(100_000, 999_999))
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone
