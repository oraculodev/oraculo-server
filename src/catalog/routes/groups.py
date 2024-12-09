from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from catalog.models import Group
from catalog.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ["get", "head"]
    ordering_fields = "__all__"
    search_fields = [
        "name",
        "description",
    ]
    filterset_fields = [
        "type",
        "is_active",
    ]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
