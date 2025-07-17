from rest_framework import serializers
from collection_management.models import CollectionManagement

class CollectionManagementListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CollectionManagement
        fields='__all__'

class CollectionManagementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=CollectionManagement
        fields='__all__'

class CollectionManagementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CollectionManagement
        fields='__all__'
        