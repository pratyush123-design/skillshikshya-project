from rest_framework.routers import DefaultRouter
from activity_management.viewsets.viewsets import ActivityManagementViewSet
router=DefaultRouter()
router.register('activity_management',ActivityManagementViewSet,basename='activity_management')


