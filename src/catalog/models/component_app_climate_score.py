from django.db import models

from catalog.models.app_climate_score import AppClimateScore
from catalog.models.component import Component
from core.models import BaseModel


class ComponentAppClimateScore(BaseModel):
    class Meta:
        verbose_name = "Component - App Climate Score"
        verbose_name_plural = "Component - App Climate Scores"
        unique_together = (("component", "app_climate_score"),)

    component = models.ForeignKey(
        Component,
        on_delete=models.CASCADE,
        verbose_name="component",
        related_name="component_app_climate_scores",
        blank=False,
        null=False,
        default=None,
    )
    app_climate_score = models.ForeignKey(
        AppClimateScore,
        on_delete=models.CASCADE,
        verbose_name="score",
        related_name="app_climate_scores",
        blank=False,
        null=False,
        default=None,
    )
    score = models.PositiveSmallIntegerField(
        "score",
        default=0,
    )

    def __str__(self):
        return self.app_climate_score.name.upper()
