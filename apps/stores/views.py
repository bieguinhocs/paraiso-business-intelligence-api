from rest_framework import viewsets, permissions
from .models import (
    StoreChannel,
    StoreRetail,
    StoreCoverage,
    Store
)
from .serializers import (
    StoreChannelSerializer,
    StoreRetailSerializer,
    StoreCoverageSerializer,StoreSerializer
)

class StoreChannelViewSet(viewsets.ModelViewSet):
    queryset = StoreChannel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StoreChannelSerializer

class StoreRetailViewSet(viewsets.ModelViewSet):
    queryset = StoreRetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StoreRetailSerializer

class StoreCoverageViewSet(viewsets.ModelViewSet):
    queryset = StoreCoverage.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StoreCoverageSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StoreSerializer
