from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, filters
from users.serializers import RegisterSerializer, UserSerializer
from users.models import User
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(
    request=RegisterSerializer,
    responses={201: None, 400: None}
)
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFilterView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['country', 'email', 'first_name', 'last_name', 'is_instructor', 'is_master']
    ordering_fields = ['email', 'first_name']
    search_fields = ['email', 'first_name', 'last_name']
