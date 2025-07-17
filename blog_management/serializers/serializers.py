from rest_framework import serializers
from blog_management.models import BLog

class BLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model=BLog
        fields='__all__'

class BLogRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=BLog
        fields='__all__'

class BLogWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=BLog
        fields='__all__'
        