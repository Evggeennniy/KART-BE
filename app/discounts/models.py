from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class ProductDiscount(models.Model):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='discounts',
        verbose_name=_("Product")
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount (%)"))
    active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    start_date = models.DateTimeField(verbose_name=_("Start Date"))
    end_date = models.DateTimeField(verbose_name=_("End Date"))

    def is_valid(self):
        now = timezone.now()
        return self.active and self.start_date <= now <= self.end_date

    class Meta:
        verbose_name = _("Product Discount")
        verbose_name_plural = _("Product Discounts")

    def __str__(self):
        return f"{self.name} - {self.value}%"


class CategoryDiscount(models.Model):
    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE,
        related_name='discounts',
        verbose_name=_("Category")
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount (%)"))
    active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    start_date = models.DateTimeField(verbose_name=_("Start Date"))
    end_date = models.DateTimeField(verbose_name=_("End Date"))

    def is_valid(self):
        now = timezone.now()
        return self.active and self.start_date <= now <= self.end_date

    class Meta:
        verbose_name = _("Category Discount")
        verbose_name_plural = _("Category Discounts")

    def __str__(self):
        return f"{self.name} - {self.value}%"
