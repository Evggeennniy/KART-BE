from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    position = models.CharField(
        max_length=32, blank=True, null=True, verbose_name=_("Position")
    )
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_("Phone number")
    )
    notes = models.TextField(
        blank=True, null=True, verbose_name=_("Notes")
    )
    country = models.CharField(
        max_length=32, blank=True, null=True, verbose_name=_("Country")
    )
    city = models.CharField(
        max_length=32, blank=True, null=True, verbose_name=_("City")
    )

    is_instructor = models.BooleanField(
        default=False, verbose_name=_("Instructor status")
    )
    is_master = models.BooleanField(
        default=False, verbose_name=_("Master status")
    )
    is_active = models.BooleanField(
        default=True, verbose_name=_("Active")
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Contact(models.Model):
    SOCIAL_NETWORK_CHOICES = [
        ('instagram', _("Instagram")),
        ('facebook', _("Facebook")),
        ('tiktok', _("TikTok")),
        ('telegram', _("Telegram")),
        ('whatsapp', _("WhatsApp")),
        ('viber', _("Viber")),
        ('linkedin', _("LinkedIn")),
        ('youtube', _("YouTube")),
        ('snapchat', _("Snapchat")),
        ('twitter', _("Twitter")),
        ('other', _("Other")),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name=_("User")
    )
    contact_type = models.CharField(
        max_length=20,
        choices=SOCIAL_NETWORK_CHOICES,
        verbose_name=_("Contact type")
    )
    value = models.CharField(
        max_length=255,
        verbose_name=_("Value")
    )
    note = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Note")
    )

    def __str__(self):
        return f"{self.user.username} — {self.get_contact_type_display()}"

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
