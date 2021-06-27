from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .filter import BookFilter
from .models import Publisher, Writer, Book
from .serializers import PublisherSerializer, WriterSerializer, BookSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [AllowAny]


class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes = [AllowAny]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
