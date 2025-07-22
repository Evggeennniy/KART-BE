from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product


class OrderList(models.Model):
    payment_method = models.CharField(max_length=64, verbose_name=_("Payment Method"))
    delivery_price = models.IntegerField(verbose_name=_("Delivery Price"))
    notes = models.TextField(blank=True, verbose_name=_("Notes"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return f"Order #{self.id}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ['-created_at']


class OrderedObject(models.Model):
    order = models.ForeignKey(
        OrderList,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name=_("Order")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='ordered_objects',
        verbose_name=_("Product")
    )
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
    sale_price = models.IntegerField(verbose_name=_("Sale Price"))
    discounted_price = models.IntegerField(verbose_name=_("Discounted Price"))

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = _("Ordered Object")
        verbose_name_plural = _("Ordered Objects")
