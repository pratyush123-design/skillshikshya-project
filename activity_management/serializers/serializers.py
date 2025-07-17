from rest_framework import serializers
from activity_management.models import ActivityManagement

class ActivityManagementListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityManagement
        fields='__all__'

class ActivityManagementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityManagement
        fields='__all__'

class ActivityManagementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityManagement
        fields='__all__'