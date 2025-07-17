from rest_framework import serializers
from booking_management.models import BookingManagement

class BookingManagementListSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingManagement
        fields='__all__'

class BookingManagementRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingManagement
        fields='__all__'

class BookingManagementWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingManagement
        fields='__all__'
        