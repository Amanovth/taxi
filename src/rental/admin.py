from django.contrib import admin
from .models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    model = Rental

# admin.site.register(Call)
# admin.site.register(AcceptCall)

# @admin.register(Rental)
# class RentalAdmin(DoubleGisAdmin):
#     list_display = ('address',)
#     list_display_links = list_display
