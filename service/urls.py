from django.urls import path, include

from .views import ServiceViewSet, CategoryViewSet, SubcategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service', ServiceViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubcategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]