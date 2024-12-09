
from django.db import models

from core.models import BaseModel


class AppClimateCategory(BaseModel):
    class Meta:
        verbose_name = "App Climate Category"
        verbose_name_plural = "App Climate Categories"

    name = models.CharField("name", max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
