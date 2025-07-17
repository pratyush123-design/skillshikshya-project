from rest_framework.routers import DefaultRouter
from cost_item.viewsets.viewsets import CostItemViewSet
router=DefaultRouter()
router.register('cost_item',CostItemViewSet,basename='cost_item')


