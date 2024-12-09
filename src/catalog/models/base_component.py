from django.db import models
from taggit.managers import TaggableManager

from core.models import BaseModel


class BaseComponent(BaseModel):
    class Meta:
        abstract = True

    name = models.CharField("name", max_length=100)
    description = models.TextField("description", max_length=255, blank=True)
    tags = TaggableManager("tags", blank=True)
