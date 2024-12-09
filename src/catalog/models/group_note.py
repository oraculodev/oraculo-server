from django.db import models

from catalog.models.base_note import BaseNote
from catalog.models.group import Group


class GroupNote(BaseNote):

    component = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="group",
        related_name="notes",
        null=False,
        default=None,
    )
