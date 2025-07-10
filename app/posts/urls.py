from django.urls import path
from posts.views import BlogPostListView, BlogPostDetailView, GalleryPhotoPostListView, GalleryPhotoPostDetailView

urlpatterns = [
    path('blog-posts/', BlogPostListView.as_view(), name='post-list'),
    path('blog-posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('gallery-posts/', GalleryPhotoPostListView.as_view(), name='gallery-post-list'),
    path('gallery-posts/<int:pk>/', GalleryPhotoPostDetailView.as_view(), name='gallery-post-detail'),

]
