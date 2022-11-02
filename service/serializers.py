from rest_framework import serializers

from service.models import Service, Category, Subcategory


class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='Account.name')

    class Meta:
        model = Service
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('title',)

