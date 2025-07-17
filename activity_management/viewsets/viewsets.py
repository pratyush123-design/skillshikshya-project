from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from activity_management.models import ActivityManagement
from activity_management.serializers.serializers import (
    ActivityManagementListSerializer,
    ActivityManagementRetrieveSerializer,
    ActivityManagementWriteSerializer,
)

class ActivityManagementViewSet(viewsets.ModelViewSet):
    queryset = ActivityManagement.objects.all()
    serializer_class = ActivityManagementListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'package']
    ordering_fields = ['name', 'package', 'description']
    filterset_fields = {
        'name': ['exact'],
        'package': ['exact'],
        'location': ['exact'],
        'description': ['exact']
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ActivityManagementWriteSerializer
        elif self.action == 'retrieve':
            return ActivityManagementRetrieveSerializer
        return ActivityManagementListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
