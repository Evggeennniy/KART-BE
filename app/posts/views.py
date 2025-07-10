from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import BlogPost, GalleryPhotoPost, GalleryVideoPost
from posts.serializers import BlogPostSerializer, GalleryPhotoPostSerializer, GalleryVideoPostSerializer


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class GalleryPhotoPostListView(ListAPIView):
    queryset = GalleryPhotoPost.objects.all()
    serializer_class = GalleryPhotoPostSerializer


class GalleryPhotoPostDetailView(RetrieveAPIView):
    queryset = GalleryPhotoPost.objects.all()
    serializer_class = GalleryPhotoPostSerializer


class GalleryVideoPostListView(ListAPIView):
    queryset = GalleryVideoPost.objects.all()
    serializer_class = GalleryVideoPostSerializer


class GalleryVideoPostDetailView(RetrieveAPIView):
    queryset = GalleryVideoPost.objects.all()
    serializer_class = GalleryVideoPostSerializer
