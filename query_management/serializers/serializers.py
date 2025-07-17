from rest_framework import serializers
from query_management.models import Query

class QueryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Query
        fields='__all__'

class QueryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Query
        fields='__all__'

class QueryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Query
        fields='__all__'
        