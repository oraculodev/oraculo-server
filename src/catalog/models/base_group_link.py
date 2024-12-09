from django.db import models

from core.models import BaseModel


class BaseGroupLink(BaseModel):
    class Meta:
        abstract = True
        verbose_name = "Group Link"
        verbose_name_plural = "Group Links"

    name = models.CharField("name", max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
