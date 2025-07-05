from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from forms.serializers import ApplicationFormSerializer
from drf_spectacular.utils import extend_schema
from forms.models import DealerApplicationForm, InstructorApplicationForm
from forms.serializers import ApplicationFormSerializer, DealerApplicationFormSerializer, InstructorApplicationFormSerializer


@extend_schema(
    request=ApplicationFormSerializer,
    responses={201: None, 400: None}
)
class ApplicationFormView(APIView):
    def post(self, request):
        serializer = ApplicationFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Заявка принята"}, status=201)


class DealerApplicationCreateView(generics.CreateAPIView):
    queryset = DealerApplicationForm.objects.all()
    serializer_class = DealerApplicationFormSerializer


class InstructorApplicationFormView(generics.CreateAPIView):
    queryset = InstructorApplicationForm.objects.all()
    serializer_class = InstructorApplicationFormSerializer
