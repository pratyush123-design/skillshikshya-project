from rest_framework import viewsets
from faqs.models import FAQs
from faqs.serializers.serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQs.objects.all()
    serializer_class = FAQSerializer