from .models import DealerApplicationForm
from rest_framework import serializers
from forms.models import ApplicationForm, InstructorApplicationForm


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = '__all__'
        read_only_fields = ['created_at']


class DealerApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerApplicationForm
        fields = '__all__'
        read_only_fields = ['created_at']


class InstructorApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorApplicationForm
        fields = "__all__"
        read_only_fields = ["created_at"]
