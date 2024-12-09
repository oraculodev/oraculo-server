from rest_framework import serializers

from catalog.models.component_app_climate_score import ComponentAppClimateScore
from catalog.serializers.app_climate_score import AppClimateScoreSerializer


class ComponentAppClimateScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentAppClimateScore
        fields = [
            "id",
            "app_climate_score",
            "score",
        ]

    app_climate_score = AppClimateScoreSerializer(read_only=True)
