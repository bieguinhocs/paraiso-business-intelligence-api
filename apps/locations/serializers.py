from rest_framework import serializers
from .models import AddressDepartment, AddressCity, AddressZoneGroup, AddressDistrict, Address

class AddressDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDepartment
        fields = '__all__'
        read_only_fields = ('created_at', )

class AddressCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCity
        fields = '__all__'
        read_only_fields = ('created_at', )

class AddressZoneGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressZoneGroup
        fields = '__all__'
        read_only_fields = ('created_at', )

class AddressDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDistrict
        fields = '__all__'
        read_only_fields = ('created_at', )

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        read_only_fields = ('created_at', )
