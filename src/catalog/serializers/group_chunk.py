from rest_framework import serializers

from catalog.models import Group


class GroupChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "type",
            "is_active",
        ]
