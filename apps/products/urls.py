from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    ProductGroupViewSet,
    ProductFamilyViewSet,
    ProductBrandViewSet,
    ProductLineViewSet,
    ProductSizeViewSet,
    ProductColorViewSet,
    ProductViewSet,
    load_lines
)

router = DefaultRouter()
router.register(r'groups', ProductGroupViewSet)
router.register(r'families', ProductFamilyViewSet)
router.register(r'brands', ProductBrandViewSet)
router.register(r'lines', ProductLineViewSet)
router.register(r'sizes', ProductSizeViewSet)
router.register(r'colors', ProductColorViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ajax/load-lines/', load_lines, name='ajax_load_lines'),
]
