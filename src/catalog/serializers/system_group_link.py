from rest_framework import serializers

from catalog.models.system_group_link import SystemGroupLink
from catalog.serializers.system_link import SystemLinkSerializer


class SystemGroupLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemGroupLink
        fields = [
            "id",
            "name",
            "links",
        ]

    links = SystemLinkSerializer(many=True, read_only=True)
