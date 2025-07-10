from django.urls import path
from posts.views import BlogPostListView, BlogPostDetailView, GalleryPhotoPostListView, GalleryPhotoPostDetailView, GalleryVideoPostListView, GalleryVideoPostDetailView

urlpatterns = [
    path('blog-posts/', BlogPostListView.as_view(), name='post-list'),
    path('blog-posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('gallery-photo-posts/', GalleryPhotoPostListView.as_view(), name='gallery-post-list'),
    path('gallery-photo-posts/<int:pk>/', GalleryPhotoPostDetailView.as_view(), name='gallery-post-detail'),
    path('gallery-video-posts/', GalleryVideoPostListView.as_view(), name='gallery-video-post-list'),
    path('gallery-video-posts/<int:pk>/', GalleryVideoPostDetailView.as_view(), name='gallery-video-post-detail'),

]
