from django.contrib import admin
from .models import ProductDiscount, CategoryDiscount
from django.utils.translation import gettext_lazy as _


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'value', 'active', 'start_date', 'end_date')
    list_filter = ('active', 'start_date', 'end_date')
    search_fields = ('name', 'product__name')


@admin.register(CategoryDiscount)
class CategoryDiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'value', 'active', 'start_date', 'end_date')
    list_filter = ('active', 'start_date', 'end_date')
    search_fields = ('name', 'category__name')
