from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ProductListView(ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'is_popular']
    ordering_fields = ['id', 'code', 'price', 'name', 'stock']
    search_fields = ['id', 'name', 'code']


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.select_related('category', 'additional_recomendations').all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
