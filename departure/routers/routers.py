from rest_framework.routers import DefaultRouter
from departure.viewsets.viewsets import DepartureViewSet
router=DefaultRouter()
router.register('departure',DepartureViewSet,basename='departure')