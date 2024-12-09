from rest_framework import serializers

from catalog.models import AppClimateItem
from catalog.serializers.app_cliamte_category import AppClimateCategorySerializer


class AppClimateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppClimateItem
        fields = [
            "name",
            "doc_url",
            "category",
        ]

    category = AppClimateCategorySerializer(read_only=True)
