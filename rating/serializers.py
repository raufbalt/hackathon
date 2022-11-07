from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
	service = serializers.ReadOnlyField(source='service.experience')
	owner = serializers.ReadOnlyField(source='owner.email')

	class Meta:
		model = Review
		fields = "__all__"