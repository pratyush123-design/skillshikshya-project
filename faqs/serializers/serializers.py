from rest_framework import serializers
from faqs.models import FAQs
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model=FAQs
        fields='__all__'
        