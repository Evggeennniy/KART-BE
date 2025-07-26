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
    role = serializers.CharField(required=True)
    certificate = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'country',
            'password',
            'role',
            'certificate',
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
            country=validated_data.get('country', ''),
            role=validated_data.get('role', ''),
            certificate=validated_data.get('certificate')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'display_name',
            'country_code',
            'phone_number',
            'email',
            'role',
            'certificate',
        ]


class UserDeliveryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'delivery_first_name',
            'delivery_last_name',
            'company_name',
            'id_or_vat_number',
            'delivery_country_region',
            'delivery_city',
            'delivery_street_address',
            'delivery_aprt_number',
            'delivery_postal_code',
            'delivery_country_code',
            'delivery_email',
            'delivery_phone_number',
            'eori_number',
        ]
class ChangePasswordSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    new_password = serializers.CharField(write_only=True, min_length=8, max_length=128)