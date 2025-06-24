from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    preview_image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name=_("Preview Image")
    )
    title = models.CharField(
        max_length=64,
        verbose_name=_("Title")
    )
    link = models.URLField(
        max_length=200,
        verbose_name=_("Link")
    )
