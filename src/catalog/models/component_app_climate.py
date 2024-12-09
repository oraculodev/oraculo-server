from django.db import models

from catalog.models.app_climate_item import AppClimateItem
from catalog.models.component import Component
from core.models import BaseModel


class ComponentAppClimate(BaseModel):
    class Meta:
        verbose_name = "Component - App Climate"
        verbose_name_plural = "Components - App Climate"
        unique_together = (("component", "app_climate_item"),)

    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
        verbose_name="component",
        related_name="app_climate_components",
        blank=False,
        null=False,
        default=None,
    )
    app_climate_item = models.ForeignKey(
        AppClimateItem,
        on_delete=models.CASCADE,
        verbose_name="item",
        related_name="app_climate_components",
        blank=False,
        null=False,
        default=None,
    )
    is_check = models.BooleanField(
        "is check",
        default=False,
    )
    not_apply = models.BooleanField(
        "not apply",
        default=False,
    )

    def __str__(self):
        return self.app_climate_item.category.name.upper()

    def item_doc_url(self):
        return self.app_climate_item.doc_url
