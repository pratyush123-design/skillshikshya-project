from rest_framework import serializers
from cost_item.models import CostItem

class CostItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CostItem
        fields='__all__'

class CostItemRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=CostItem
        fields='__all__'

class CostItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CostItem
        fields='__all__'
        