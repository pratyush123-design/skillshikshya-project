from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from package_management.models import PackageManagement
from package_management.serializers.package_management_serializers import (
    PackageManagementListSerializer,
    PackageManagementRetrieveSerializer,
    PackageManagementWriteSerializer,
)

class PackageManagementViewSet(viewsets.ModelViewSet):
    queryset = PackageManagement.objects.all()
    serializer_class = PackageManagementListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'name']
    filterset_fields = {
        'price': ['exact'],
        'name': ['exact'],
        'status': ['exact'],
        'feature_image': ['exact']
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PackageManagementWriteSerializer
        elif self.action == 'retrieve':
            return PackageManagementRetrieveSerializer
        return PackageManagementListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
