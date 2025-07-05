from rest_framework.generics import ListAPIView
from info.models import FAQ
from info.serializers import FAQSerializer


class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
