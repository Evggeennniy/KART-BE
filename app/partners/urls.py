from django.urls import path
from partners.views import DealerListView, DealerDetailView, InstructorListView, InstructorDetailView, MasterListView, MasterDetailView

urlpatterns = [
    path('dealers/', DealerListView.as_view(), name='dealer-list'),
    path('dealers/<int:pk>/', DealerDetailView.as_view(), name='dealer-detail'),
    path('instructors/', InstructorListView.as_view(), name='instructor-list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('masters/', MasterListView.as_view(), name='master-list'),
    path('masters/<int:pk>/', MasterDetailView.as_view(), name='master-detail'),
]
