from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    ProductGroupViewSet,
    ProductFamilyViewSet,
    ProductLineViewSet,
    ProductBrandViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router.register(r'groups', ProductGroupViewSet)
router.register(r'families', ProductFamilyViewSet)
router.register(r'lines', ProductLineViewSet)
router.register(r'brands', ProductBrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
