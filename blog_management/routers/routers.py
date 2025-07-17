from rest_framework.routers import DefaultRouter
from blog_management.viewsets.viewsets import BLogViewSet
router=DefaultRouter()
router.register('blog_management',BLogViewSet,basename='blog_management')