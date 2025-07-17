from rest_framework.routers import DefaultRouter
from faqs.viewsets.viewsets import FAQViewSet
router=DefaultRouter()
router.register('faqs',FAQViewSet,basename='faqs')