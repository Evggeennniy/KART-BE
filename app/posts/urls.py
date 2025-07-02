from django.urls import path
from posts.views import BlogPostListView, BlogPostDetailView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post-list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
]
