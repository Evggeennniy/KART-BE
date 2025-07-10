from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import RegisterSerializer
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
