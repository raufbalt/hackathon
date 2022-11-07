from rest_framework import serializers
from service.models import Service, Category, Review, Favorite


class ServiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')

    class Meta:
        model = Service
        fields = '__all__'

    def validate(self, attrs):
        a = self._context['request']
        if a.user.status != 2:
            raise serializers.ValidationError(
                'You are not executor!'
            )
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ReviewSerializer(serializers.ModelSerializer):
    service = serializers.ReadOnlyField(source='service.experience')
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Review
        fields = "__all__"


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    service = serializers.ReadOnlyField(source='service.experience')

    class Meta:
        model = Favorite
        fields = '__all__'

