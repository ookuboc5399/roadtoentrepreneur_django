from rest_framework import generics
from .serializers import BookSerializer
from .models import Books
from rest_framework.permissions import AllowAny


class BookView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

class BookDetailView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)