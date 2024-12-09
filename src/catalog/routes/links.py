from rest_framework import filters, viewsets

from catalog.models import Link
from catalog.serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    http_method_names = ["get", "head"]
    ordering_fields = "__all__"
    search_fields = [
        "title",
        "description",
    ]
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )
