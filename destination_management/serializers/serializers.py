from rest_framework import serializers
from destination_management.models import Destination

class DestinationListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Destination
        fields='__all__'

class DestinationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Destination
        fields='__all__'

class DestinationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Destination
        fields='__all__'
        