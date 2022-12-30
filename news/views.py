from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import NewsSerializer
from .models import News


class NewsView(generics.ListAPIView):
    queryset = News.objects.all().order_by("-created_at")[:2]
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)
