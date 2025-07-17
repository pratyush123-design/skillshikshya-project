from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from gear_item.models import GearItem
from gear_item.serializers.serializers import (
    GearItemListSerializer,
    GearItemRetrieveSerializer,
    GearItemWriteSerializer,
)

class GearItemViewSet(viewsets.ModelViewSet):
    queryset = GearItem.objects.all()
    serializer_class = GearItemListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination','name']
    ordering_fields = ['description', 'required']
    filterset_fields = {
        'destination': ['exact'],
        'name': ['exact'],
        
        
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return GearItemWriteSerializer
        elif self.action == 'retrieve':
            return GearItemRetrieveSerializer
        return GearItemListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
