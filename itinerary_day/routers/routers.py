from rest_framework.routers import DefaultRouter
from itinerary_day.viewsets.viewsets import ItineraryDayViewSet
router=DefaultRouter()
router.register('itinerary_day',ItineraryDayViewSet,basename='itinerary_day')