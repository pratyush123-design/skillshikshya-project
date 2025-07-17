from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog_management.models import BLog
from blog_management.serializers.serializers import (
    BLogListSerializer,
    BLogRetrieveSerializer,
    BLogWriteSerializer,
)

class BLogViewSet(viewsets.ModelViewSet):
    queryset = BLog.objects.all()
    serializer_class = BLogListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['is_popular']
    filterset_fields = {
        'title': ['exact'],
        'is_popular': ['exact'],
        
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BLogWriteSerializer
        elif self.action == 'retrieve':
            return BLogRetrieveSerializer
        return BLogListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
