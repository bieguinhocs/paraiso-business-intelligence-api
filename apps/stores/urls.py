from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StoreChannelViewSet,
    StoreRetailViewSet,
    StoreCoverageViewSet,
    StoreViewSet
)

router = DefaultRouter()
router.register(r'channels', StoreChannelViewSet)
router.register(r'retails', StoreRetailViewSet)
router.register(r'coverages', StoreCoverageViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
