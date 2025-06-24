from rest_framework import serializers
from .models import Post


class PostReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = fields  # всё только для чтения
