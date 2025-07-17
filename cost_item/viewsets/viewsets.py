from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from cost_item.models import CostItem
from cost_item.serializers.serializers import (
    CostItemListSerializer,
    CostItemRetrieveSerializer,
    CostItemWriteSerializer,
)

class CostItemViewSet(viewsets.ModelViewSet):
    queryset = CostItem.objects.all()
    serializer_class = CostItemListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['amount', 'label']
    ordering_fields = ['amount', 'label', 'currency']
    filterset_fields = {
        'destination': ['exact'],
        'amount': ['exact'],
        'label': ['exact'],
        'currency': ['exact']
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CostItemWriteSerializer
        elif self.action == 'retrieve':
            return CostItemRetrieveSerializer
        return CostItemListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
