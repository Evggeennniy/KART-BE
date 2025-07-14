from rest_framework.generics import ListAPIView, RetrieveAPIView
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.http import Http404

class ProductListView(ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category__slug', 'is_popular']
    ordering_fields = ['id', 'code', 'price', 'name', 'stock']
    search_fields = ['id', 'name', 'code']


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('additional_recomendations').all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="products",
            description="Список ID продуктов через запятую:",
            required=True,
            type=str,
            location=OpenApiParameter.QUERY,
        )
    ],
    responses={200: None, 404: None}
)
class ActualPricesView(APIView):
    def get(self, request):
        ids_string = request.query_params.get("products")
        if not ids_string:
            raise Http404("products parameter required")

        product_ids = []
        for i in ids_string.split(","):
            if i.isdigit():
                product_ids.append(int(i))

        products = Product.objects.filter(id__in=product_ids)

        result = []
        for product in products:
            result.append({
                "id": product.id,
                "title": product.name,
                "price": int(product.price),
                "image": product.image.url if product.image else ""
            })

        return Response(result, status=200)