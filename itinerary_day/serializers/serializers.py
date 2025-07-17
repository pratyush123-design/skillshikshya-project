from rest_framework import serializers
from itinerary_day.models import ItineraryDay

class ItineraryDayListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItineraryDay
        fields='__all__'

class ItineraryDayRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItineraryDay
        fields='__all__'

class ItineraryDayWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItineraryDay
        fields='__all__'
        