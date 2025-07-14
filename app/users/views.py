import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import ( RegisterSerializer,
                                UserPersonalDetailsSerializer,
                                UserDeliveryDetailsSerializer,
                                ChangePasswordSerializer )
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from django.shortcuts import get_object_or_404
from users.models import User

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

@extend_schema(
    request=UserPersonalDetailsSerializer,
    responses={
        200: UserPersonalDetailsSerializer,
        400: OpenApiResponse(description="Bad request"),
        401: OpenApiResponse(description="Unauthorized"),
    }
)

class UserPersonalDetailsView(APIView):
    serializer_class = UserPersonalDetailsSerializer

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=UserDeliveryDetailsSerializer,
    responses={
        200: UserDeliveryDetailsSerializer,
        400: OpenApiResponse(description="Bad request"),
        401: OpenApiResponse(description="Unauthorized"),
    }
)


class UserDeliveryDetailsView(APIView):
    serializer_class = UserDeliveryDetailsSerializer

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    def patch(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@extend_schema(
    parameters=[
        OpenApiParameter(
            name="email",
            description="Email користувача для відновлення паролю",
            required=True,
            type=str,
            location=OpenApiParameter.QUERY,
        )
    ],
    responses={
        200: OpenApiResponse(description='UUID generated'),
        400: OpenApiResponse(description='Email missing'),
        404: OpenApiResponse(description='User not found'),
    }
)
class ForgotPasswordView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({"detail": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            user.uuid = uuid.uuid4()
            user.save()
            return Response({"uuid": str(user.uuid)}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@extend_schema(
    request=ChangePasswordSerializer,
    responses={
        200: OpenApiResponse(description='Password changed successfully'),
        400: OpenApiResponse(description='Invalid data'),
        404: OpenApiResponse(description='User not found by UUID')
    }
)
class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            uuid_value = serializer.validated_data['uuid']
            new_password = serializer.validated_data['new_password']

            user = get_object_or_404(User, uuid=uuid_value)
            user.set_password(new_password)
            user.uuid = uuid.uuid4()

            return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)