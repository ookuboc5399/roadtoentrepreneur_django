from rest_framework import viewsets
from rest_framework import generics
from .serializers import VideoSerializer
from rest_framework.permissions import AllowAny
from .models import Video


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer