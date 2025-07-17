from rest_framework.routers import DefaultRouter
from destination_management.viewsets.viewsets import DestinationViewSet
router=DefaultRouter()
router.register('destination_management',DestinationViewSet,basename='destination_management')