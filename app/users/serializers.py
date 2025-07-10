from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import User


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    country = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'country',
            'password',
        ]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Емаил уже зарегистрирован.")
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            country=validated_data.get('country', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
