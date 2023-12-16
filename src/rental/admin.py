from django.contrib import admin
from .models import Rental

admin.site.register(Rental)

# @admin.register(Rental)
# class RentalAdmin(DoubleGisAdmin):
#     list_display = ('address',)
#     list_display_links = list_display
