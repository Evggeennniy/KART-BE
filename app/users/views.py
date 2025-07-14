from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import RegisterSerializer, UserPersonalDetailsSerializer, UserDeliveryDetailsSerializer
from drf_spectacular.utils import extend_schema


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


class UserPersonalDetailsView(APIView):
    serializer_class = UserPersonalDetailsSerializer

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


class UserDeliveryDetailsView(APIView):
    serializer_class = UserDeliveryDetailsSerializer

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
