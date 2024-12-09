from catalog.serializers.role import RoleSerializer
from rest_framework import serializers

from catalog.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            "id",
            "name",
            "email",
            "role",
        ]

    role = RoleSerializer(read_only=True)