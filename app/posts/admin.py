from django.contrib import admin
from posts.models import BlogPost
from django.utils.translation import gettext_lazy as _


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)

    fieldsets = (
        (None, {
            'fields': ('title', 'link', 'preview_image'),
        }),
    )
