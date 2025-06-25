from django.urls import path
from dealers.views import DealerListView, DealerDetailView

urlpatterns = [
    path('dealers/', DealerListView.as_view(), name='dealer-list'),
]
