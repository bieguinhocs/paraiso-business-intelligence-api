from rest_framework import viewsets, permissions
from .models import AddressDepartment, AddressCity, AddressZonalGroup, AddressDistrict, Address
from .serializers import (
    AddressDepartmentSerializer,
    AddressCitySerializer,
    AddressZonalGroupSerializer,
    AddressDistrictSerializer,
    AddressSerializer
)

class AddressDepartmentViewSet(viewsets.ModelViewSet):
    queryset = AddressDepartment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AddressDepartmentSerializer

class AddressCityViewSet(viewsets.ModelViewSet):
    queryset = AddressCity.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AddressCitySerializer

class AddressZonalGroupViewSet(viewsets.ModelViewSet):
    queryset = AddressZonalGroup.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AddressZonalGroupSerializer

class AddressDistrictViewSet(viewsets.ModelViewSet):
    queryset = AddressDistrict.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AddressDistrictSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AddressSerializer
