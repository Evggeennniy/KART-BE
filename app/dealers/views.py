from rest_framework.generics import ListAPIView
from dealers.models import Dealer
from dealers.serializers import DealerSerializer


class DealerListView(ListAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
