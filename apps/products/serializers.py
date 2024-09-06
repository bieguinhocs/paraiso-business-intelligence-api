from rest_framework import serializers
from .models import (
    ProductGroup,
    ProductFamily,
    ProductLine,
    ProductBrand,
    Product
)

class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'
        read_only_fields = ('created_at', )

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

class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'
        read_only_fields = ('created_at', )

class ProductSerializer(serializers.ModelSerializer):
    brand = ProductBrandSerializer()
    family = ProductFamilySerializer()
    line = ProductLineSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', )
