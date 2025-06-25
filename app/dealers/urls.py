from django.urls import path
from dealers.views import DealerListView

urlpatterns = [
    path('', DealerListView.as_view(), name='dealer-list'),
]
