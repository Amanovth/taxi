from django.contrib import admin
from .models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'tarif', 'passenger', 'driver', 'point_a_street', 'point_b_street']
    list_display_links = ['id', 'status', 'tarif', 'passenger', 'driver']

# admin.site.register(Call)
# admin.site.register(AcceptCall)

# @admin.register(Rental)
# class RentalAdmin(DoubleGisAdmin):
#     list_display = ('address',)
#     list_display_links = list_display
