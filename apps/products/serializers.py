from rest_framework import serializers
from .models import (
    ProductGroup,
    ProductFamily,
    ProductBrand,
    ProductLine,
    ProductSize,
    ProductColor,
    Product
)

class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductFamilySerializer(serializers.ModelSerializer):
    group = ProductGroupSerializer()
    class Meta:
        model = ProductFamily
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductLineSerializer(serializers.ModelSerializer):
    brand = ProductBrandSerializer()
    class Meta:
        model = ProductLine
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductSerializer(serializers.ModelSerializer):
    size = ProductSizeSerializer()
    color = ProductColorSerializer()
    line = ProductLineSerializer()
    family = ProductFamilySerializer()
    #retail = serializers.PrimaryKeyRelatedField(queryset=StoreRetail.objects.all(), allow_null=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', )
        