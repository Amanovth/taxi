from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.admin import TokenAdmin, TokenProxy
from .models import User

admin.site.unregister(TokenProxy)


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('user_type', 'phone', 'password', 'code', 'activated')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Bank card'), {'fields': ('card_num', 'valid', 'cvv')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone", "password1", "password2", "groups", "is_staff"),
            },
        ),
    )

    list_display = ('id', 'phone', 'user_type', 'first_name', 'last_name', 'last_login',)
    list_display_links = ('id', 'phone',)
    ordering = ('-id',)
