from django.db import models

from catalog.models.base_note import BaseNote
from catalog.models.component import Component


class ComponentNote(BaseNote):

    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
        verbose_name="component",
        related_name="notes",
        null=False,
        default=None,
    )
