from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import BlogPost, GalleryPhotoPost
from posts.serializers import BlogPostSerializer, GalleryPhotoPostSerializer


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
