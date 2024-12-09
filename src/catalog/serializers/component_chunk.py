from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from catalog.models import Component
from catalog.serializers.component_app_climate_score import (
    ComponentAppClimateScoreSerializer,
)
from catalog.serializers.component_note import ComponentNoteSerializer
from catalog.serializers.group_chunk import GroupChunkSerializer
from catalog.serializers.macroarea import MacroareaSerializer
from catalog.serializers.system_chunk import SystemChunkSerializer


class ComponentChunkSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = [
            "id",
            "name",
            "repo_url",
            "type",
            "group_owner",
            "lifecycle",
            "system",
            "context_level",
            "macroarea",
            "critical",
            "tags",
            "component_app_climate_scores",
            "notes",
            "created_at",
            "updated_at",
        ]

    group_owner = GroupChunkSerializer(read_only=True)
    system = SystemChunkSerializer(read_only=True)
    macroarea = MacroareaSerializer(read_only=True)
    tags = TagListSerializerField()
    component_app_climate_scores = ComponentAppClimateScoreSerializer(
        many=True, read_only=True
    )
    notes = ComponentNoteSerializer(many=True, read_only=True)
