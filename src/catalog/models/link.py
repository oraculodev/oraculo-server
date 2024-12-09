from django.db import models

from core.models import BaseModel


class Link(BaseModel):
    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    title = models.CharField("title", max_length=50, blank=False, null=False)
    description = models.TextField("description", max_length=255, blank=False, null=False)
    icon = models.CharField("icon (boxicons)", max_length=50, blank=False, null=False)
    url = models.URLField("url", blank=False, null=False)

    def __str__(self):
        return self.title
