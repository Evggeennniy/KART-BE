from rest_framework import serializers
from forms.models import ApplicationForm


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['name', 'email', 'phone_number', 'message']
