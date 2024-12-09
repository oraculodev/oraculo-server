from rest_framework import serializers


class DashSerializer(serializers.Serializer):
    production_services_count = serializers.IntegerField()
    critical_services_count = serializers.IntegerField()
    not_up_to_date_services_count = serializers.IntegerField()
    services_by_group = serializers.JSONField()
    services_count_by_type = serializers.JSONField()
    services_count_by_macroarea = serializers.JSONField()
