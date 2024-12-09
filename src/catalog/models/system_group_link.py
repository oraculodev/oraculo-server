from django.db import models

from catalog.models.base_group_link import BaseGroupLink
from catalog.models.system import System


class SystemGroupLink(BaseGroupLink):

    system = models.ForeignKey(
        System,
        on_delete=models.CASCADE,
        verbose_name="system",
        related_name="group_links",
        null=True,
        default=None,
    )
