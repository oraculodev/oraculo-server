from django.db import models

from catalog.models.resource_type import ResourceType
from core.models import BaseModel
from catalog.shared.choices import LifecycleTypes


class Resource(BaseModel):
    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"


    name = models.CharField("name", max_length=100)
    description = models.TextField("description", max_length=255, blank=True)

    type = models.ForeignKey(
        ResourceType,
        on_delete=models.DO_NOTHING,
        verbose_name="type",
        related_name="resources",
        null=True,
        blank=True,
    )

    lifecycle = models.CharField(
        "lifecycle",
        max_length=50,
        choices=LifecycleTypes.choices,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name
