from django.db import models

from core.models import BaseModel


class Macroarea(BaseModel):
    class Meta:
        verbose_name = "Macroarea"
        verbose_name_plural = "Macroareas"

    name = models.CharField("name", max_length=50)

    def __str__(self):
        return self.name
