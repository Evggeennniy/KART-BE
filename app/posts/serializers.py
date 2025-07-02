from rest_framework import serializers
from posts.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['preview_image', 'title', 'link']
        read_only_fields = fields
