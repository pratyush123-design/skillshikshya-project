from rest_framework.routers import DefaultRouter
from review_management.viewsets.viewsets import ReviewViewSet
router=DefaultRouter()
router.register('review_management',ReviewViewSet,basename='review_management')
