from modeltranslation.translator import register, TranslationOptions
from posts.models import BlogPost, GalleryPost


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(GalleryPost)
class GalleryPostTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
