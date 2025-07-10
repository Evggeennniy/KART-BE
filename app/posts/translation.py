from modeltranslation.translator import register, TranslationOptions
from posts.models import BlogPost, GalleryPhotoPost, GalleryVideoPost


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(GalleryPhotoPost)
class GalleryPostTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(GalleryVideoPost)
class GalleryPostTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
