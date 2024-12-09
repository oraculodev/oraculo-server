from rest_framework import serializers

from catalog.models import System


class SystemChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = [
            "id",
            "name",
        ]
