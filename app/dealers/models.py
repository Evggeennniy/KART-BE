from django.db import models
from django.utils.translation import gettext_lazy as _


class Dealer(models.Model):
    image = models.ImageField(
        upload_to='countries/',
        blank=True,
        null=True,
        verbose_name=_("Image")
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Name")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Dealer")
        verbose_name_plural = _("Dealers")
