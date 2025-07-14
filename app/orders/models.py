from django.db import models
from products.models import Product

class OrderedObject(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_objects')
    quantity = models.PositiveIntegerField()
    sale_price = models.IntegerField()
    discounted_price = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class OrderList(models.Model):
    included = models.ManyToManyField(OrderedObject, related_name='orders')
    payment_method = models.CharField(max_length=64)
    delivery_price = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id}"