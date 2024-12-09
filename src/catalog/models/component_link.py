from django.db import models

from catalog.models.base_link import BaseLink
from catalog.models.component_group_link import ComponentGroupLink


class ComponentLink(BaseLink):

    group_link = models.ForeignKey(
        ComponentGroupLink,
        on_delete=models.CASCADE,
        verbose_name="link",
        related_name="links",
        null=True,
        default=None,
    )
