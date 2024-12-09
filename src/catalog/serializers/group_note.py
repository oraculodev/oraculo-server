from rest_framework import serializers

from catalog.models.group_note import GroupNote


class GroupNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupNote
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]
