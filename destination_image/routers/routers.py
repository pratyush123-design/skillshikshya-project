from rest_framework.routers import DefaultRouter
from destination_image.viewsets.viewsets import DestinationImageViewSet
router=DefaultRouter()
router.register('destination_image',DestinationImageViewSet,basename='destination_image')