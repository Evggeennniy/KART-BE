from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Contact
from django.utils.translation import gettext_lazy as _


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    fields = ('contact_type', 'value', 'note')
    verbose_name = _("Contact")
    verbose_name_plural = _("Contacts")


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    inlines = [ContactInline]

    list_display = ('username', 'email', 'is_instructor', 'is_master', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_master', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_("Personal info"), {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'phone_number',
                'position',
                'country',
                'city',
                'notes',
            )
        }),
        (_("Permissions"), {'fields': (
            'is_active',
            'is_instructor',
            'is_master',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (_("Important dates"), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'phone_number',
                'position',
                'country',
                'city',
                'notes',
                'is_instructor',
                'is_master',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
            ),
        }),
    )
