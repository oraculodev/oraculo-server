from rest_framework import filters, viewsets

from catalog.models import System
from catalog.serializers import SystemSerializer


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    http_method_names = ["get", "head"]
    ordering_fields = "__all__"
    search_fields = [
        "name",
        "description",
        "tags__name",
    ]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
