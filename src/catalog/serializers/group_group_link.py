from rest_framework import serializers

from catalog.models.group_group_link import GroupGroupLink
from catalog.serializers.group_link import GroupLinkkSerializer


class GroupGroupLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupGroupLink
        fields = [
            "id",
            "name",
            "links",
        ]

    links = GroupLinkkSerializer(many=True, read_only=True)
