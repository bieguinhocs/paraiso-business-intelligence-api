from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AddressDepartmentViewSet,
    AddressCityViewSet,
    AddressZonalGroupViewSet,
    AddressDistrictViewSet,
    AddressViewSet
)

router = DefaultRouter()
router.register(r'departments', AddressDepartmentViewSet)
router.register(r'cities', AddressCityViewSet)
router.register(r'zonal-groups', AddressZonalGroupViewSet)
router.register(r'districts', AddressDistrictViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
