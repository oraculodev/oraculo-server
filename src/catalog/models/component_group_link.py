from django.db import models

from catalog.models.base_group_link import BaseGroupLink
from catalog.models.component import Component


class ComponentGroupLink(BaseGroupLink):

    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
        verbose_name="component",
        related_name="group_links",
        null=True,
        default=None,
    )
