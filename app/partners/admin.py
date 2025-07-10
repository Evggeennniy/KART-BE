from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import gettext_lazy as _
from partners.models import Dealer, Instructor, Master, Contact


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('country', 'company_name', 'email', 'website', 'whats_app', 'viber')
    search_fields = ('country', 'company_name', 'email', 'website')
    list_filter = ('country', 'company_name')

    exclude = ('country', 'company_name', 'adress')

    class Meta:
        verbose_name = _("Dealer")
        verbose_name_plural = _("Dealers")


class ContactInline(GenericTabularInline):
    model = Contact
    extra = 1


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'email')
    inlines = [ContactInline]

    exclude = ('first_name', 'last_name', 'country', 'position')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'email')
    inlines = [ContactInline]

    exclude = ('first_name', 'last_name', 'country', 'position')
