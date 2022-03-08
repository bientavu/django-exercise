from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from sales.models import Sale, Article
from sales.pagination import CustomPagination
from sales.serializers import SaleSerializer, ArticleSerializer, SalesListBy25Serializer
from sales.permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Display the default Article view
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


class SaleViewSet(viewsets.ModelViewSet):
    """
    Display the default Sale view
    """
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class SalesListBy25ViewSet(viewsets.ModelViewSet):
    """
    Display the Sale view with custom options (pagination & fields)
    """
    queryset = Sale.objects.all()
    serializer_class = SalesListBy25Serializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination
