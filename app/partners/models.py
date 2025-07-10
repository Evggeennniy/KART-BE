from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext_lazy as _


class Dealer(models.Model):
    image = models.ImageField(
        upload_to='partners/dealers/',
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


class Instructor(models.Model):
    image = models.ImageField(
        upload_to='partners/instructors/',
        verbose_name=_("Image")
    )
    first_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Last Name")
    )
    country = models.CharField(
        max_length=32,
        blank=True,
        verbose_name=_("Country")
    )
    position = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Position")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description")
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        verbose_name=_("Email")
    )
    phone = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("Phone")
    )
    contacts = GenericRelation('Contact', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _("Instructor")
        verbose_name_plural = _("Instructors")


class Master(models.Model):
    image = models.ImageField(
        upload_to='partners/masters/',
        verbose_name=_("Image")
    )
    first_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Last Name")
    )
    country = models.CharField(
        max_length=32,
        blank=True,
        verbose_name=_("Country")
    )
    position = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Position")
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description")
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        verbose_name=_("Email")
    )
    phone = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("Phone")
    )
    contacts = GenericRelation('Contact', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _("Master")
        verbose_name_plural = _("Masters")


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

    # Generic relation
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    contact_object = GenericForeignKey('content_type', 'object_id')

    contact_type = models.CharField(max_length=20, choices=SOCIAL_NETWORK_CHOICES, verbose_name=_("Contact type"))
    value = models.CharField(max_length=255, verbose_name=_("Value"))
    note = models.TextField(blank=True, null=True, verbose_name=_("Note"))

    def __str__(self):
        return f"{self.contact_object} — {self.get_contact_type_display()}"

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
