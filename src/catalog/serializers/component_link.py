from rest_framework import serializers

from catalog.models.component_link import ComponentLink


class ComponentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentLink
        fields = [
            "id",
            "text",
            "url",
        ]
