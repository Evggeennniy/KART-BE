from rest_framework import serializers
from dealers.models import Dealer  # Убедись, что импорт правильный


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'image', 'name']
