from email.policy import default

from django.db import models

from catalog.models.app_climate_category import AppClimateCategory
from core.models import BaseModel


class AppClimateItem(BaseModel):
    class Meta:
        verbose_name = "App Climate Item"
        verbose_name_plural = "App Climate Items"

    name = models.CharField("name", max_length=100, blank=False, null=False)
    category = models.ForeignKey(
        AppClimateCategory,
        on_delete=models.DO_NOTHING,
        verbose_name="category",
        related_name="app_climate_items",
        null=False,
        blank=False,
        default=0,
    )
    doc_url = models.URLField("documentation url", blank=True, null=True)

    def __str__(self):
        return self.name
