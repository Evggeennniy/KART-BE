import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_("Email address"))

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True, blank=True)

    position = models.CharField(max_length=64, blank=True, null=False, default="", verbose_name=_("Position"))
    notes = models.TextField(blank=True, null=False, default="", verbose_name=_("Notes"))
    country = models.CharField(max_length=32, blank=True, null=False, default="", verbose_name=_("Country"))
    country_code = models.CharField(max_length=16, blank=True, null=False, default="", verbose_name=_("Country Code"))
    phone_number = models.CharField(max_length=32, blank=True, null=False, default="", verbose_name=_("Phone Number"))
    city = models.CharField(max_length=64, blank=True, null=False, default="", verbose_name=_("City / Locality"))
    display_name = models.CharField(max_length=64, blank=True, null=False, default="", verbose_name=_("Display Name"))

    delivery_first_name = models.CharField(max_length=16, blank=True, null=False,
                                           default="", verbose_name=_("Delivery Name"))
    delivery_last_name = models.CharField(max_length=16, blank=True, null=False,
                                          default="", verbose_name=_("Delivery Last Name"))
    company_name = models.CharField(max_length=128, blank=True, null=False, default="", verbose_name=_("Company Name"))
    id_or_vat_number = models.CharField(max_length=64, blank=True, null=False,
                                        default="", verbose_name=_("ID/VAT Number"))
    delivery_country_region = models.CharField(
        max_length=64, blank=True, null=False, default="", verbose_name=_("Country/Region"))
    delivery_city = models.CharField(max_length=16, blank=True, null=False,
                                     default="", verbose_name=_("City / Locality"))
    delivery_street_address = models.CharField(
        max_length=255, blank=True, null=False, default="", verbose_name=_("Street Address"))
    delivery_aprt_number = models.CharField(max_length=16, blank=True, null=False,
                                            default="", verbose_name=_("Apartment Number"))
    delivery_postal_code = models.CharField(max_length=16, blank=True, null=False,
                                            default="", verbose_name=_("Postal Code"))
    delivery_email = models.EmailField(blank=True, null=False, default="", verbose_name=_("Delivery Email"))
    delivery_country_code = models.CharField(max_length=16, blank=True, null=False,
                                             default="", verbose_name=_("Delivery Country Code"))
    delivery_phone_number = models.CharField(max_length=32, blank=True, null=False,
                                             default="", verbose_name=_("Delivery Phone Number"))
    eori_number = models.CharField(max_length=64, blank=True, null=False, default="", verbose_name=_("EORI Number"))

    is_instructor = models.BooleanField(default=False, verbose_name=_("Instructor status"))
    is_master = models.BooleanField(default=False, verbose_name=_("Master status"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
