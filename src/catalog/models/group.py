from django.db import models
from tinymce import models as tinymce_models

from catalog.models.base_component import BaseComponent
from catalog.models.member import Member
from catalog.shared.choices import GroupTypes


class Group(BaseComponent):
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    description = tinymce_models.HTMLField()
    parent = models.ForeignKey(
        "Group",
        on_delete=models.DO_NOTHING,
        verbose_name="pai",
        null=True,
        blank=True,
    )
    type = models.CharField(
        "type",
        max_length=50,
        choices=GroupTypes.choices,
        null=True,
        blank=True,
        default=None,
    )

    is_active = models.BooleanField("is active", default=True)
    board_url = models.URLField("board url", blank=True, null=True)
    design_url = models.URLField("design url", blank=True, null=True)

    members = models.ManyToManyField(
        Member,
        verbose_name="members",
        related_name="groups",
        blank=True,
    )

    other_components = models.ManyToManyField(
        "component",
        verbose_name="other components",
        related_name="groups",
        blank=True,
    )

    def __str__(self):
        return self.name

    def related_groups(self):
        return Group.objects.filter(parent=self)
