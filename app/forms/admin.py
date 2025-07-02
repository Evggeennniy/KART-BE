from django.contrib import admin
from forms.models import ApplicationForm


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message')
    search_fields = ('name', 'email', 'phone_number')
