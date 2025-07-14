from rest_framework import serializers
from .models import OrderedObject, OrderList
from products.models import Product

class OrderedObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedObject
        fields = ['id', 'product', 'quantity', 'sale_price', 'discounted_price']


class OrderListSerializer(serializers.ModelSerializer):
    included = OrderedObjectSerializer(many=True)

    class Meta:
        model = OrderList
        fields = ['id', 'included', 'payment_method', 'delivery_price', 'notes']

    def create(self, validated_data):
        included_data = validated_data.pop('included')
        order = OrderList.objects.create(**validated_data)
        for item in included_data:
            product = item['product']
            ordered_obj = OrderedObject.objects.create(**item)
            order.included.add(ordered_obj)
        return order
