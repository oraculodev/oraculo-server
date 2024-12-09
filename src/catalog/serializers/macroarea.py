from rest_framework import serializers

from catalog.models.macroarea import Macroarea


class MacroareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macroarea
        fields = [
            "id",
            "name",
        ]
