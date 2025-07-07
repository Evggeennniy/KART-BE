from modeltranslation.translator import register, TranslationOptions
from products.models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('id', 'name')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description',
        'how_to_use',
        'ingredients',
    )
