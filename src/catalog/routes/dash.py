from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from catalog.controllers.component_controller import get_dashboard_data
from catalog.serializers.dash import DashSerializer


class DashViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DashSerializer
    http_method_names = ["get", "head"]

    def list(self, request):
        results = DashSerializer(get_dashboard_data(), read_only=True, many=True).data
        return Response(results)

    def get_queryset(self):
        return []
