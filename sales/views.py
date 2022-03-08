from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from sales.models import Sale, Article
from sales.pagination import CustomPagination
from sales.serializers import SaleSerializer, ArticleSerializer, SalesListBy25Serializer
from sales.permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class SalesListBy25ViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalesListBy25Serializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination



#     def create_article(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# @api_view(['GET'])
# def sales_list(request):
#     sales = Sale.objects.all()
#     serializer_class = SaleSerializer(sales, many=True)
#     return Response(serializer_class)
