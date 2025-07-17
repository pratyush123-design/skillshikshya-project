from rest_framework.routers import DefaultRouter
from home_page.viewsets.viewsets import HomePageViewSet
router=DefaultRouter()
router.register('home_page',HomePageViewSet,basename='home_page')