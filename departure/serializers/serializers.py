from rest_framework import serializers
from departure.models import Departure

class DepartureListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departure
        fields='__all__'

class DepartureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departure
        fields='__all__'

class DepartureWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departure
        fields='__all__'
        