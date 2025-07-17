from rest_framework.routers import DefaultRouter
from package_management.viewsets.package_management_viewsets import PackageManagementViewSet
router=DefaultRouter()
router.register('package_management',PackageManagementViewSet,basename='package_management')

