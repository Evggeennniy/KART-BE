from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from products.models import Category, Product
from django.utils.translation import get_language


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_editable = ()

    exclude = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_editable = ()

    exclude = (
        'name',
        'description',
        'how_to_use',
        'ingredients',
    )
