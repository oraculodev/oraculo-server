from django.db import models

from catalog.models.base_link import BaseLink
from catalog.models.group_group_link import GroupGroupLink


class GroupLink(BaseLink):

    group_link = models.ForeignKey(
        GroupGroupLink,
        on_delete=models.CASCADE,
        verbose_name="link",
        related_name="links",
        null=True,
        default=None,
    )
