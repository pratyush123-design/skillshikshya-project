from rest_framework.routers import DefaultRouter
from query_management.viewsets.viewsets import QueryViewSet
router=DefaultRouter()
router.register('query_management',QueryViewSet,basename='query_management')

