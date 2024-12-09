from rest_framework import serializers

from catalog.models import ComponentAppClimate
from catalog.serializers.app_climate_item import AppClimateItemSerializer


class ComponentAppClimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentAppClimate
        fields = [
            "id",
            "app_climate_item",
            "is_check",
            "not_apply",
        ]

    app_climate_item = AppClimateItemSerializer(read_only=True)
