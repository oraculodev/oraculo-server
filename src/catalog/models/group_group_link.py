from django.db import models

from catalog.models.base_group_link import BaseGroupLink
from catalog.models.group import Group


class GroupGroupLink(BaseGroupLink):

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="group",
        related_name="group_links",
        null=True,
        default=None,
    )
