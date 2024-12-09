from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from catalog.models import Component
from catalog.serializers.component_app_climate_score import (
    ComponentAppClimateScoreSerializer,
)
from catalog.serializers.component_chunk import ComponentChunkSerializer
from catalog.serializers.component_group_link import ComponentGroupLinkSerializer
from catalog.serializers.component_note import ComponentNoteSerializer
from catalog.serializers.group_chunk import GroupChunkSerializer
from catalog.serializers.macroarea import MacroareaSerializer
from catalog.serializers.resource import ResourceSerializer
from catalog.serializers.system_chunk import SystemChunkSerializer


class ComponentSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = [
            "id",
            "name",
            "description",
            "repo_url",
            "repo_created_at",
            "repo_updated_at",
            "repo_pushed_at",
            "tags",
            "type",
            "group_owner",
            "lifecycle",
            "system",
            "context_level",
            "macroarea",
            "critical",
            "cicd_url",
            "api_doc_url",
            "public_api_doc_url",
            "is_filled",
            "created_at",
            "updated_at",
            "components",
            "group_links",
            "notes",
            "component_app_climate_scores",
            "resources",
        ]

    group_owner = GroupChunkSerializer(read_only=True)
    system = SystemChunkSerializer(read_only=True)
    macroarea = MacroareaSerializer(read_only=True)
    components = ComponentChunkSerializer(many=True, read_only=True)
    group_links = ComponentGroupLinkSerializer(many=True, read_only=True)
    tags = TagListSerializerField()
    component_app_climate_scores = ComponentAppClimateScoreSerializer(
        many=True, read_only=True
    )
    resources = ResourceSerializer(many=True, read_only=True)
    notes = ComponentNoteSerializer(many=True, read_only=True)
