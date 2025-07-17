from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from collection_management.models import CollectionManagement
from collection_management.serializers.serializers import (
    CollectionManagementListSerializer,
    CollectionManagementRetrieveSerializer,
    CollectionManagementWriteSerializer,
)

class CollectionManagementViewSet(viewsets.ModelViewSet):
    queryset = CollectionManagement.objects.all()
    serializer_class = CollectionManagementListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination','name']
    ordering_fields = ['name']
    filterset_fields = {
        'destination': ['exact'],
        'name': ['exact'],
        
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CollectionManagementWriteSerializer
        elif self.action == 'retrieve':
            return CollectionManagementRetrieveSerializer
        return CollectionManagementListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
