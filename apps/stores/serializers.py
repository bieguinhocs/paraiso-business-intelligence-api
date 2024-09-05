from rest_framework import serializers
from .models import (
    StoreChannel,
    StoreRetail,
    StoreCoverage,
    Store
)

class StoreChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreChannel
        fields = '__all__'
        read_only_fields = ('created_at', )

class StoreRetailSerializer(serializers.ModelSerializer):
    channel = StoreChannelSerializer(read_only=True)

    class Meta:
        model = StoreRetail
        fields = '__all__'
        read_only_fields = ('created_at', )

class StoreCoverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCoverage
        fields = '__all__'
        read_only_fields = ('created_at', )

class StoreSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(read_only=True)
    coordinator = serializers.PrimaryKeyRelatedField(read_only=True)
    retail = StoreRetailSerializer(read_only=True)
    coverage = StoreCoverageSerializer(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ('created_at', )
