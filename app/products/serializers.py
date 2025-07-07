from rest_framework import serializers
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = fields


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    additional_recomendations = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'how_to_use',
            'ingredients',
            'code',
            'price',
            'stock',
            'image',
            'category',
            'additional_recomendations'
        ]
        read_only_fields = fields

    def get_additional_recomendations(self, obj):
        qs = obj.additional_recomendations.all()
        if not qs:
            return []
        return ProductShortSerializer(qs, many=True, context=self.context).data
