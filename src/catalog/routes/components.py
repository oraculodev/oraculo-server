from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.mixins import NestedViewSetMixin

from catalog.models import Component
from catalog.models.component_app_climate import ComponentAppClimate
from catalog.models.component_app_climate_score import ComponentAppClimateScore
from catalog.serializers import ComponentSerializer
from catalog.serializers.component_app_climate import ComponentAppClimateSerializer
from catalog.serializers.component_app_climate_score import (
    ComponentAppClimateScoreSerializer,
)


class ComponentViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    http_method_names = ["get", "head"]
    ordering_fields = "__all__"
    search_fields = [
        "name",
        "description",
        "tags__name",
    ]
    filterset_fields = [
        "type",
        "lifecycle",
        "critical",
        "group_owner",
    ]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )


class ComponentAppClimateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ComponentAppClimate.objects.all()
    serializer_class = ComponentAppClimateSerializer
    http_method_names = ["get", "head"]
    ordering_fields = "__all__"
    filterset_fields = ["app_climate_item__category"]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )


class ComponentAppClimateScoreViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ComponentAppClimateScore.objects.all()
    serializer_class = ComponentAppClimateScoreSerializer
    http_method_names = ["get", "head"]
    ordering_fields = "__all__"
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
