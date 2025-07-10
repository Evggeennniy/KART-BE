from rest_framework import serializers
from partners.models import Dealer, Contact, Instructor, Master


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = [
            'image',
            'country',
            'company_name',
            'adress',
            'website',
            'email',
            'whats_app',
            'viber',
            'instagram',
            'facebook'
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ['content_type', 'object_id']


class InstructorSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Instructor
        fields = [
            'id', 'first_name', 'last_name', 'country', 'position',
            'description', 'email', 'phone', 'image', 'contacts'
        ]


class MasterSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Master
        fields = [
            'id', 'first_name', 'last_name', 'country', 'position',
            'description', 'email', 'phone', 'image', 'contacts'
        ]
