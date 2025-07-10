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
    position = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("Position"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))
    country = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("City"))
    is_instructor = models.BooleanField(default=False, verbose_name=_("Instructor status"))
    is_master = models.BooleanField(default=False, verbose_name=_("Master status"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
