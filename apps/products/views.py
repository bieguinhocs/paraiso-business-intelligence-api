from rest_framework import viewsets, permissions
from .models import (
    ProductGroup,
    ProductFamily,
    ProductLine,
    ProductBrand,
    Product
)
from .serializers import (
    ProductGroupSerializer,
    ProductFamilySerializer,
    ProductLineSerializer,
    ProductBrandSerializer,
    ProductSerializer,
)

class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = ProductGroup.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductGroupSerializer

class ProductFamilyViewSet(viewsets.ModelViewSet):
    queryset = ProductFamily.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductFamilySerializer

class ProductLineViewSet(viewsets.ModelViewSet):
    queryset = ProductLine.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductLineSerializer

class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductBrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
