from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from catalog.models import Group
from catalog.serializers.component_chunk import ComponentChunkSerializer
from catalog.serializers.group_chunk import GroupChunkSerializer
from catalog.serializers.group_group_link import GroupGroupLinkSerializer
from catalog.serializers.group_note import GroupNoteSerializer
from catalog.serializers.member import MemberSerializer


class GroupSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "description",
            "is_active",
            "tags",
            "type",
            "parent",
            "board_url",
            "design_url",
            "components",
            "other_components",
            "members",
            "created_at",
            "updated_at",
            "group_links",
            "related_groups",
            "notes",
        ]

    group_links = GroupGroupLinkSerializer(many=True, read_only=True)
    components = serializers.SerializerMethodField()
    other_components = ComponentChunkSerializer(many=True, read_only=True)
    members = serializers.SerializerMethodField()
    tags = TagListSerializerField()
    related_groups = GroupChunkSerializer(many=True, read_only=True)
    notes = GroupNoteSerializer(many=True, read_only=True)

    def get_members(self, instance):
        members = instance.members.all().order_by("role", "name")
        return MemberSerializer(members, many=True, read_only=True).data

    def get_components(self, instance):
        components = instance.components.all().order_by("-critical", "name")
        return ComponentChunkSerializer(components, many=True, read_only=True).data
