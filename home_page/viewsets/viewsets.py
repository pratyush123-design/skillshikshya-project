from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from home_page.models import HomePage
from home_page.serializers.serializers import (
    HomePageListSerializer,
    HomePageRetrieveSerializer,
    HomePageWriteSerializer,
)

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    ordering_fields = [ 'total_days']
    filterset_fields = {
        
        'title': ['exact'],
       
          }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return HomePageWriteSerializer
        elif self.action == 'retrieve':
            return HomePageRetrieveSerializer
        return HomePageListSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
