from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from destination_image.models import DestinationImage
from destination_image.serializers.serializers import (
    DestinationImageListSerializer,
    DestinationImageRetrieveSerializer,
    DestinationImageWriteSerializer,
)

class DestinationImageViewSet(viewsets.ModelViewSet):
    queryset = DestinationImage.objects.all()
    serializer_class = DestinationImageListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination','image']
    ordering_fields = ['image', 'caption']
    filterset_fields = {
        'destination': ['exact'],
        'image': ['exact'],
        'caption': ['exact'],
        
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DestinationImageWriteSerializer
        elif self.action == 'retrieve':
            return DestinationImageRetrieveSerializer
        return DestinationImageListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
