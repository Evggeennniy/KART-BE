from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from dealers.models import Dealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ()
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'image')
        }),
    )

    verbose_name = _("Dealer")
    verbose_name_plural = _("Dealers")
