from django.db import models
from django.utils.translation import gettext_lazy as _


class Dealer(models.Model):
    image = models.ImageField(
        upload_to='countries/',
        verbose_name=_("Image")
    )
    country = models.CharField(
        max_length=16,
        unique=True,
        verbose_name=_("Country")
    )
    company_name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name=_("Company")
    )
    adress = models.CharField(
        max_length=255,
        verbose_name=_("Address")
    )
    website = models.URLField(
        max_length=255,
        blank=True,
        verbose_name=_("Website")
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        verbose_name=_("Email")
    )
    whats_app = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("WhatsApp")
    )
    viber = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("Viber")
    )
    instagram = models.URLField(
        max_length=255,
        blank=True,
        verbose_name=_("Instagram")
    )
    facebook = models.URLField(
        max_length=255,
        blank=True,
        verbose_name=_("Facebook")
    )

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = _("Dealer")
        verbose_name_plural = _("Dealers")
