from rest_framework import serializers
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]
        read_only_fields = fields


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

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
        ]
        read_only_fields = fields
