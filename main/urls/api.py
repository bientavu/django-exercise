from django.urls import path, include
from sales.urls import router as sales_router

from rest_framework import routers


router = routers.DefaultRouter()
router.registry.extend(sales_router.registry)

urlpatterns = [
    path("", include(router.urls)),
]

# urlpatterns = [
#     path(
#         "v1/",
#         include(
#             [
#                 path("", include(router.urls)),
#             ]
#         ),
#     ),
# ]
