from modeltranslation.translator import register, TranslationOptions
from partners.models import Dealer, Instructor, Master


@register(Dealer)
class DealerTranslationOptions(TranslationOptions):
    fields = (
        'country',
        'company_name',
        'adress'
    )


@register(Instructor)
class InstructorTranslationOptions(TranslationOptions):
    fields = (
        'first_name',
        'last_name',
        'country',
        'position',
    )


@register(Master)
class MasterTranslationOptions(TranslationOptions):
    fields = (
        'first_name',
        'last_name',
        'country',
        'position',
    )
