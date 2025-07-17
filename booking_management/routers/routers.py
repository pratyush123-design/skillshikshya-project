from rest_framework.routers import DefaultRouter
from booking_management.viewsets.viewsets import BookingManagementViewSet
router=DefaultRouter()
router.register('booking_management',BookingManagementViewSet,basename='booking_management')
