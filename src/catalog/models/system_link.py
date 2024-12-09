from django.db import models

from catalog.models.base_link import BaseLink
from catalog.models.system_group_link import SystemGroupLink


class SystemLink(BaseLink):

    group_link = models.ForeignKey(
        SystemGroupLink,
        on_delete=models.CASCADE,
        verbose_name="link",
        related_name="links",
        null=True,
        default=None,
    )
