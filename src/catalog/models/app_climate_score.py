from django.db import models

from catalog.models.app_climate_category import AppClimateCategory
from core.models import BaseModel


class AppClimateScore(BaseModel):
    class Meta:
        verbose_name = "App Climate Score"
        verbose_name_plural = "App Climate Scores"

    name = models.CharField("name", max_length=100, blank=False, null=False)
    categories = models.ManyToManyField(
        AppClimateCategory,
        verbose_name="categories",
        blank=True,
    )

    def __str__(self):
        return self.name


class CalculateAppClimateScore:
    def __init__(self, app_climate_score: AppClimateScore):
        self.app_climate_score = app_climate_score
        self.components_count = 0
        self.components_checked_count = 0

    def get_score(self):
        if self.components_count == 0 or self.components_checked_count == 0:
            return 0

        return round((self.components_checked_count * 100) / self.components_count)

    def reset(self):
        self.components_count = 0
        self.components_checked_count = 0
