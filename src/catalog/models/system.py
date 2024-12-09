from django.db import models

from catalog.models.base_component import BaseComponent
from catalog.models.group import Group
from catalog.shared.choices import LifecycleTypes


class System(BaseComponent):
    class Meta:
        verbose_name = "System"
        verbose_name_plural = "Systems"

    lifecycle = models.CharField(
        "lifecycle",
        max_length=50,
        choices=LifecycleTypes.choices,
        null=True,
        blank=True,
        default=None,
    )

    groups = models.ManyToManyField(Group, verbose_name="groups", blank=True)

    def __str__(self):
        return self.name
