from django.urls import path, include

from .views import ServiceViewSet, CategoryViewSet, FavoriteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service', ServiceViewSet)
router.register('categories', CategoryViewSet)
router.register('favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls))
]