from rest_framework import serializers

from catalog.models.resource_type import ResourceType


class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        fields = [
            "id",
            "name",
        ]
