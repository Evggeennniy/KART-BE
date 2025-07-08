from rest_framework import serializers
from dealers.models import Dealer


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
