from django.contrib import admin
from .models import Driver, Tariff


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["id", "get_user", "user", "status", "city", "car_tariff", "star"]
    list_display_links = ['id', 'get_user', 'user']

    def get_user(self, obj):
        if obj.user:
            return obj.user.first_name
        return None

    get_user.short_description = 'Имя'

admin.site.register(Tariff)
