from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from catalog.models.system import System
from catalog.serializers.component_chunk import ComponentChunkSerializer
from catalog.serializers.group_chunk import GroupChunkSerializer
from catalog.serializers.system_group_link import SystemGroupLinkSerializer


class SystemSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = System
        fields = [
            "id",
            "name",
            "description",
            "tags",
            "lifecycle",
            "groups",
            "group_links",
            "components",
            "created_at",
            "updated_at",
        ]

    tags = TagListSerializerField()
    groups = GroupChunkSerializer(many=True, read_only=True)
    group_links = SystemGroupLinkSerializer(many=True, read_only=True)
    components = ComponentChunkSerializer(many=True, read_only=True)
