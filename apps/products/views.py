from rest_framework import viewsets, permissions
from .models import (
    ProductGroup,
    ProductFamily,
    ProductBrand,
    ProductLine,
    ProductSize,
    ProductColor,
    Product
)
from .serializers import (
    ProductGroupSerializer,
    ProductFamilySerializer,
    ProductBrandSerializer,
    ProductLineSerializer,
    ProductSizeSerializer,
    ProductColorSerializer,
    ProductSerializer,
)
from django.http import JsonResponse

class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = ProductGroup.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductGroupSerializer

class ProductFamilyViewSet(viewsets.ModelViewSet):
    queryset = ProductFamily.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductFamilySerializer

class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductBrandSerializer

class ProductLineViewSet(viewsets.ModelViewSet):
    queryset = ProductLine.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductLineSerializer

class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSizeSerializer

class ProductColorViewSet(viewsets.ModelViewSet):
    queryset = ProductColor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductColorSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

def load_lines(request):
    brand_id = request.GET.get('brand')
    lines = ProductLine.objects.filter(brand_id=brand_id).order_by('name')
    return JsonResponse(list(lines.values('id', 'name')), safe=False)