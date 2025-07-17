from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from query_management.models import Query
from query_management.serializers.serializers import (
    QueryListSerializer,
    QueryRetrieveSerializer,
    QueryWriteSerializer,
)

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QueryListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price']
    filterset_fields = {
        
        'name': ['exact'],
        'phone_number': ['exact'],
      
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return QueryWriteSerializer
        elif self.action == 'retrieve':
            return QueryRetrieveSerializer
        return QueryListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
