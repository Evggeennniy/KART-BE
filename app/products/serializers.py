from rest_framework import serializers
from products.models import Product, Category
from drf_spectacular.utils import extend_schema_field


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = fields


class ProductShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image1', 'price', 'slug']


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
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'category',
            'additional_recomendations',
            'slug'
        ]
        read_only_fields = fields

    @extend_schema_field(ProductShortSerializer(many=True))
    def get_additional_recomendations(self, obj):
        qs = obj.additional_recomendations.all()
        return ProductShortSerializer(qs, many=True, context=self.context).data
