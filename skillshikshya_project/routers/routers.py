from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from activity_management.viewsets.viewsets import ActivityManagementViewSet
from blog_management.viewsets.viewsets import BLogViewSet
from booking_management.viewsets.viewsets import BookingManagementViewSet
from collection_management.viewsets.viewsets import CollectionManagementViewSet
from cost_item.viewsets.viewsets import CostItemViewSet
from departure.viewsets.viewsets import DepartureViewSet
from destination_image.viewsets.viewsets import DestinationImageViewSet
from destination_management.viewsets.viewsets import DestinationViewSet
from faqs.viewsets.viewsets import FAQViewSet
from gear_item.viewsets.viewsets import GearItemViewSet
from home_page.viewsets.viewsets import HomePageViewSet
from itinerary_day.viewsets.viewsets import ItineraryDayViewSet

from package_management.viewsets.package_management_viewsets import PackageManagementViewSet
from query_management.viewsets.viewsets import QueryViewSet
from review_management.viewsets.viewsets import ReviewViewSet
from team_member.viewsets.viewsets import TeamMemberViewSet


router.register(r'faqs', FAQViewSet, basename='faqs')
router.register(r'blog_management',BLogViewSet,basename='blog_management')
router.register(r'package_management',PackageManagementViewSet,basename='package_management')
router.register(r'query_management',QueryViewSet,basename='query_management')
router.register(r'booking_management',BookingManagementViewSet,basename='book_management')
router.register(r'collection_management',CollectionManagementViewSet,basename='collection_management')
router.register(r'cost_item',CostItemViewSet,basename='cost_item')
router.register(r'departure',DepartureViewSet,basename='departure')
router.register(r'destination_image',DestinationImageViewSet,basename='destination_image')
router.register(r'destination_management',DestinationViewSet,basename='destination_management')
router.register(r'activity_management',ActivityManagementViewSet,basename='activity_management')

router.register(r'gear_item',GearItemViewSet,basename='gear_item')
router.register(r'home_page',HomePageViewSet,basename='home_page')
router.register(r'itinerary_day',ItineraryDayViewSet,basename='itinerary_day')

router.register(r'review_management',ReviewViewSet,basename='review_management')
router.register(r'team_member',TeamMemberViewSet,basename='team_member')

