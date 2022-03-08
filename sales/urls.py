from rest_framework import routers

from sales.views import SaleViewSet, ArticleViewSet, SalesListBy25ViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('sales-by-25', SalesListBy25ViewSet)
router.register('sales', SaleViewSet)
