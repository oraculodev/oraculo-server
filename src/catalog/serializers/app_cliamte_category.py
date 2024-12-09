from rest_framework import serializers

from catalog.models import AppClimateCategory


class AppClimateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppClimateCategory
        fields = [
            "name",
        ]
