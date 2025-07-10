from django.contrib import admin
from forms.models import ApplicationForm, DealerApplicationForm, InstructorApplicationForm


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message')
    search_fields = ('name', 'email', 'phone_number')


@admin.register(DealerApplicationForm)
class DealerApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'full_name', 'email', 'created_at')
    search_fields = ('company_name', 'email', 'full_name')
    list_filter = ('experience_years', 'license_status', 'has_office', 'has_training_center')
    readonly_fields = ('created_at',)


@admin.register(InstructorApplicationForm)
class InstructorApplicationFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'city', 'created_at')
    search_fields = ('full_name', 'email', 'city')
    readonly_fields = ('created_at',)
    ordering = ('created_at',)
