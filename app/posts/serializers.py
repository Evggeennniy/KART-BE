from rest_framework import serializers
from posts.models import BlogPost, GalleryPhotoPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['preview_image', 'title', 'link']
        read_only_fields = fields


class GalleryPhotoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhotoPost
        fields = ['image', 'title', 'datetime']
        read_only_fields = fields
