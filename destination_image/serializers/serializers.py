from rest_framework import serializers
from destination_image.models import DestinationImage

class DestinationImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model=DestinationImage
        fields='__all__'

class DestinationImageRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=DestinationImage
        fields='__all__'

class DestinationImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=DestinationImage
        fields='__all__'
        