from django.contrib import admin
from posts.models import BlogPost, GalleryPhotoPost, GalleryVideoPost
from django.utils.translation import gettext_lazy as _


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'link')

    exclude = ('title',)


@admin.register(GalleryPhotoPost)
class GalleryPhotoPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime')
    search_fields = ('title',)

    exclude = ('title',)


@admin.register(GalleryVideoPost)
class GalleryVideoPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime')
    search_fields = ('title',)

    exclude = ('title',)
