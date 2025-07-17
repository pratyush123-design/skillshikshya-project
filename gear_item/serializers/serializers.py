from rest_framework import serializers
from gear_item.models import GearItem

class GearItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model=GearItem
        fields='__all__'

class GearItemRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=GearItem
        fields='__all__'

class GearItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=GearItem
        fields='__all__'
        