from rest_framework import serializers

from catalog.models.component_group_link import ComponentGroupLink
from catalog.serializers.component_link import ComponentLinkSerializer


class ComponentGroupLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentGroupLink
        fields = [
            "id",
            "name",
            "links",
        ]

    links = ComponentLinkSerializer(many=True, read_only=True)
