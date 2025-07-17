from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from booking_management.models import BookingManagement
from booking_management.serializers.serializers import (
    BookingManagementListSerializer,
    BookingManagementRetrieveSerializer,
    BookingManagementWriteSerializer,
)

class BookingManagementViewSet(viewsets.ModelViewSet):
    queryset = BookingManagement.objects.all()
    serializer_class = BookingManagementListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['full_name','phone']
    ordering_fields = ['full_name']
    filterset_fields = {
        'activity_type': ['exact'],
        'full_name': ['exact'],
        
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookingManagementWriteSerializer
        elif self.action == 'retrieve':
            return BookingManagementRetrieveSerializer
        return BookingManagementListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
