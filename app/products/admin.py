from django.contrib import admin
from products.models import Category, Product
from django.forms import CharField


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')

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
