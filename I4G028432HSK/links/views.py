from rest_framework import generics
from .models import Links
from .Serizliers import PostSerializer

# Create your views here.
class PostListApi (generics.ListAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = PostSerializer

class PostCreateApi (generics.CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = PostSerializer

class PostDetailsApi (generics.RetrieveAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = PostSerializer

class PostUpdateApi (generics.UpdateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = PostSerializer

class PostDeleteApi (generics.DestroyAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = PostSerializer