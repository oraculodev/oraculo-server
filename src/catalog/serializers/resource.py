from catalog.serializers.resource_type import ResourceTypeSerializer
from rest_framework import serializers

from catalog.models.resource import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            "id",
            "name",
            "description",
            "type",
            "lifecycle",
            "created_at",
            "updated_at",
        ]

    type = ResourceTypeSerializer(read_only=True)