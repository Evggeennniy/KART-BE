from modeltranslation.translator import register, TranslationOptions
from .models import Dealer


@register(Dealer)
class DealerTranslationOptions(TranslationOptions):
    fields = (
        'country',
        'company_name',
    )
