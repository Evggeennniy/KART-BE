from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):
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

    class Meta:
        verbose_name = _("Blog post")
        verbose_name_plural = _("Blogs posts")


class GalleryPhotoPost(models.Model):
    image = models.ImageField(
        upload_to='gallery/photos/',
        blank=True,
        null=True,
        verbose_name=_("Image")
    )
    title = models.CharField(
        max_length=64,
        verbose_name=_("Title")
    )
    datetime = models.DateTimeField(
        verbose_name=_("Date and Time")
    )

    class Meta:
        verbose_name = _("Gallery Photo Post")
        verbose_name_plural = _("Gallery Photo Posts")


class GalleryVideoPost(models.Model):
    video = models.FileField(
        upload_to='gallery/photos/',
        blank=True,
        null=True,
        verbose_name=_("Image")
    )
    title = models.CharField(
        max_length=64,
        verbose_name=_("Title")
    )
    datetime = models.DateTimeField(
        verbose_name=_("Date and Time")
    )

    class Meta:
        verbose_name = _("Gallery Video Post")
        verbose_name_plural = _("Gallery Video Posts")
