from rest_framework import serializers
from service.models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='auth.user')

    class Meta:
        model = Service
        fields = "__all__"

    def validate(self, attrs):
        a = self._context['request']
        if a.user.user != 2:
            raise serializers.ValidationError(
                'You are not executor!'
            )
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

