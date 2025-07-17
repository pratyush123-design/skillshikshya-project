from rest_framework import serializers
from package_management.models import PackageManagement

class PackageManagementListSerializer(serializers.ModelSerializer):
    class Meta:
        model=PackageManagement
        fields='__all__'

class PackageManagementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=PackageManagement
        fields='__all__'

class PackageManagementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=PackageManagement
        fields='__all__'
        