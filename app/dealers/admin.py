from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from dealers.models import Dealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('country', 'company_name', 'email', 'website', 'whats_app', 'viber')
    search_fields = ('country', 'company_name', 'email', 'website')
    list_filter = ('country', 'company_name')
    ordering = ('country',)

    fieldsets = (
        (_("Основное"), {
            'fields': ('country', 'company_name', 'adress', 'image')
        }),
        (_("Контактные данные"), {
            'fields': ('email', 'website', 'whats_app', 'viber', 'instagram', 'facebook')
        }),
    )

    readonly_fields = ()

    class Meta:
        verbose_name = _("Dealer")
        verbose_name_plural = _("Dealers")
