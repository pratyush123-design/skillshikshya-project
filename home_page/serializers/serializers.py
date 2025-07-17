from rest_framework import serializers
from home_page.models import HomePage

class HomePageListSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomePage
        fields='__all__'

class HomePageRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomePage
        fields='__all__'

class HomePageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomePage
        fields='__all__'
        