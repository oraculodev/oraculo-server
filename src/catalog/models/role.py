from django.db import models

from core.models import BaseModel


class Role(BaseModel):
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    name = models.CharField("name", max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
