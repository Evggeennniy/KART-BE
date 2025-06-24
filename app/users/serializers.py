from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm')

    def create(self, validated_data):
        if validated_data['password'] == validated_data['password_confirm']:
            del validated_data['password_confirm']

            user = User.objects.create_user(**validated_data)
            return user
