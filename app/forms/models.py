from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationForm(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Applicant Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"))
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return f"Application form {self.name}"

    class Meta:
        verbose_name = _("Application Form")
        verbose_name_plural = _("Application Forms")
