from rest_framework import serializers

from catalog.models.app_climate_score import AppClimateScore


class AppClimateScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppClimateScore
        fields = [
            "name",
        ]
