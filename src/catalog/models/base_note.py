from django.db import models
from tinymce import models as tinymce_models

from core.models import BaseModel


class BaseNote(BaseModel):
    class Meta:
        abstract = True
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    title = models.CharField("title", max_length=50, blank=False, null=False)
    content = tinymce_models.HTMLField()

    def __str__(self):
        return self.title
