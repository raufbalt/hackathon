from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from .models import Service, Category
from .permissions import IsOwner
from .serializers import ServiceSerializer, CategorySerializer


class StandartResultsPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'page'
    max_page_size = 1000


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('category',)
    filterset_fields = ('category',)
    pagination_class = StandartResultsPagination

    def perform_create(self, serializer):
        data = self.request.data
        Service.objects.create(
            owner=self.request.user,
            price=self.request.data.get("price", None),
            experience=self.request.data.get("experience", None),
            hour_from=self.request.data.get("hour_from", None),
            hour_to=self.request.data.get("hour_to", None),
            desc=self.request.data.get("desc", None),
            category=self.request.data.get("category", None)

        )

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete'):
            return [IsOwner()]
        return [permissions.IsAuthenticatedOrReadOnly()]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]
