from rest_framework import serializers

from catalog.models.system_link import SystemLink


class SystemLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemLink
        fields = [
            "id",
            "text",
            "url",
        ]
