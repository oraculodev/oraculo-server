from django.db import models

from core.models import BaseModel


class BaseLink(BaseModel):
    class Meta:
        abstract = True
        verbose_name = "Link"
        verbose_name_plural = "Links"

    text = models.CharField("text", max_length=200, blank=False, null=False)
    url = models.URLField("url", blank=False, null=False)

    def __str__(self):
        return self.text
