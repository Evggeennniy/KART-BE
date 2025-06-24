from django.contrib import admin
from django.utils.html import format_html
from posts.models import Post
from django.utils.translation import gettext_lazy as _


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)

    fieldsets = (
        (None, {
            'fields': ('title', 'link', 'preview_image'),
        }),
    )
