from django.db import models

from core.models import BaseModel


class ResourceType(BaseModel):
    class Meta:
        verbose_name = "Resource Type"
        verbose_name_plural = "Resource Types"

    name = models.CharField("name", max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
