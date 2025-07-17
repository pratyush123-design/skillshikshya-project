from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from departure.models import Departure
from departure.serializers.serializers import (
    DepartureListSerializer,
    DepartureRetrieveSerializer,
    DepartureWriteSerializer,
)

class DepartureViewSet(viewsets.ModelViewSet):
    queryset = Departure.objects.all()
    serializer_class = DepartureListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['destination', 'start_date','end_date']
    ordering_fields = ['price', 'currency']
    filterset_fields = {
        'price': ['exact'],
        'currency': ['exact'],
        'start_date': ['exact'],
        'end_date': ['exact']
        
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DepartureWriteSerializer
        elif self.action == 'retrieve':
            return DepartureRetrieveSerializer
        return DepartureListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
