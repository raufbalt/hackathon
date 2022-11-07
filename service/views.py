from django.shortcuts import get_object_or_404
from rest_framework import permissions, response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from .models import Service, Category, Favorite
from .permissions import IsOwner
from .serializers import ServiceSerializer, CategorySerializer, ReviewSerializer, FavoriteSerializer


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
        category = self.request.data.get('category', None)
        category = int(category)
        category1 = get_object_or_404(Category, id=category)
        Service.objects.create(
            owner=self.request.user,
            price=self.request.data.get("price", None),
            experience=self.request.data.get("experience", None),
            hour_from=self.request.data.get("hour_from", None),
            hour_to=self.request.data.get("hour_to", None),
            desc=self.request.data.get("desc", None),
            category=category1

        )

    # api/v1/service/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        service = self.get_object()
        if request.method == 'GET':
            reviews = service.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            print(serializer.data, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            return response.Response(serializer.data, status=200)
        if service.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, service=service)
        return response.Response(serializer.data, status=201)

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


class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        data = self.request.data
        service = self.request.data.get('service', None)
        service = int(service)
        service1 = get_object_or_404(Service, id=service)
        Favorite.objects.create(
            owner=self.request.user,
            service=service1
        )