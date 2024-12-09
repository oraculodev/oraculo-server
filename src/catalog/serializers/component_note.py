from rest_framework import serializers

from catalog.models.component_note import ComponentNote


class ComponentNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentNote
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]
