from rest_framework.routers import DefaultRouter
from gear_item.viewsets.viewsets import GearItemViewSet
router=DefaultRouter()
router.register('gear_item',GearItemViewSet,basename='gear_item')