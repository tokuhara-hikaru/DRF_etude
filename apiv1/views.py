from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """本モデルのCRUD用のAPIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    Permission_classes = [IsAuthenticatedOrReadOnly]
