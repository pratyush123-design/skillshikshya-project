from rest_framework.routers import DefaultRouter
from team_member.viewsets.viewsets import TeamMemberViewSet
router=DefaultRouter()
router.register('team_member',TeamMemberViewSet,basename='team_member')

