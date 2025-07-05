# faq_app/translation.py

from modeltranslation.translator import register, TranslationOptions
from info.models import FAQ


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = (
        'question',
        'answer',
    )
