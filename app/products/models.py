from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name=_("Name")
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=_("Slug")
    )

    only_for_masters = models.BooleanField(default=False, verbose_name="Only for masters")
    cover_default_price = models.BooleanField(default=False, verbose_name="Cover default price")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Code"),
        blank=False,
        null=False
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=_("Slug")
    )
    image1 = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("Image 1")
    )
    image2 = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("Image 2")
    )
    image3 = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("Image 3")
    )
    image4 = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("Image 4")
    )
    image5 = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        verbose_name=_("Image 5")
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_("Name")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description")
    )
    how_to_use = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("How to Use")
    )
    ingredients = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Ingredients")
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price")
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Stock")
    )
    is_new = models.BooleanField(
        default=False,
        verbose_name=_("Is New")
    )
    is_popular = models.BooleanField(
        default=False,
        verbose_name=_("Is Popular")
    )
    category = models.ForeignKey(
        'Category',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name=_("Category")
    )
    additional_recomendations = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='recommended_by',
        verbose_name=_("Additional Recommendations")
    )

    def __str__(self):
        return f"{self.name} ({self.code})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
