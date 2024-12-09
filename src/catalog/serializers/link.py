from rest_framework import serializers

from catalog.models.link import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            "id",
            "title",
            "description",
            "icon",
            "url",
            "created_at",
            "updated_at",
        ]
