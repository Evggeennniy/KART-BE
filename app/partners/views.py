from rest_framework.generics import ListAPIView, RetrieveAPIView
from partners.models import Dealer, Instructor, Master
from partners.serializers import DealerSerializer, InstructorSerializer


class DealerListView(ListAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerDetailView(RetrieveAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class InstructorListView(ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorDetailView(RetrieveAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class MasterListView(ListAPIView):
    queryset = Master.objects.all()
    serializer_class = InstructorSerializer


class MasterDetailView(RetrieveAPIView):
    queryset = Master.objects.all()
    serializer_class = InstructorSerializer
