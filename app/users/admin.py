from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['email',]

    readonly_fields = ('uuid',)

    list_display = ('email', 'uuid',  'is_instructor', 'is_master', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_master', 'is_staff')

    fieldsets = (
        (None, {'fields': ('password',)}),

        (_("Personal info"), {
            'fields': (
                'first_name',
                'last_name',
                'display_name',
                'country_code',
                'phone_number',
                'email',
            )
        }),

        (_("Delivery info"), {
            'fields': (
                'delivery_first_name',
                'delivery_last_name',
                'company_name',
                'id_or_vat_number',
                'delivery_country_region',
                'delivery_city',
                'delivery_street_address',
                'delivery_aprt_number',
                'delivery_postal_code',
                'delivery_email',
                'delivery_country_code',
                'delivery_phone_number',
                'eori_number',
            )
        }),

        (_("Permissions"), {
            'fields': (
                'is_active',
                'is_instructor',
                'is_master',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        (_("Important dates"), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'country',
                'password1',
                'password2',
                'is_active',
                'is_instructor',
                'is_master',
                'is_staff',
                'is_superuser',
            ),
        }),
    )
