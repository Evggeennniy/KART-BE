from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import OrderList
from .serializers import OrderListSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(request=OrderListSerializer, responses=OrderListSerializer)
class OrderCreateView(CreateAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


@extend_schema(responses=OrderListSerializer)
class OrderDetailView(RetrieveAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'id'


@extend_schema(responses=OrderListSerializer)
class OrderListView(ListAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
