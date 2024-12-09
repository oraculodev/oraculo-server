from rest_framework import serializers

from catalog.models.group_link import GroupLink


class GroupLinkkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupLink
        fields = [
            "id",
            "text",
            "url",
        ]
