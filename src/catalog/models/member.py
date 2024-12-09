from django.db import models
from catalog.models.role import Role
from taggit.managers import TaggableManager

from core.models import BaseModel


class Member(BaseModel):
    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    name = models.CharField("name", max_length=100)
    email = models.EmailField("email", max_length=100, blank=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.DO_NOTHING,
        verbose_name="role",
        related_name="members",
        null=True,
        blank=True,
    )
    tags = TaggableManager("tags", blank=True)

    def __str__(self):
        return self.name
