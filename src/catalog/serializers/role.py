from rest_framework import serializers

from catalog.models.role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            "id",
            "name",
        ]
