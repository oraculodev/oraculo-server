from django.db import models

from catalog.models.base_component import BaseComponent
from catalog.models.group import Group
from catalog.models.macroarea import Macroarea
from catalog.models.resource import Resource
from catalog.models.system import System
from catalog.shared.choices import ComponentTypes, ContextLevel, LifecycleTypes


class Component(BaseComponent):
    class Meta:
        verbose_name = "Component"
        verbose_name_plural = "Components"

    repo_id = models.BigIntegerField("repository id", unique=True)
    repo_url = models.URLField("repository url", unique=True)
    repo_created_at = models.DateTimeField(
        "repository created at", default=None, null=True, blank=True
    )
    repo_updated_at = models.DateTimeField(
        "repository updated at", default=None, null=True, blank=True
    )
    repo_pushed_at = models.DateTimeField(
        "repository pushed at", default=None, null=True, blank=True
    )
    group_owner = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING,
        verbose_name="owner",
        related_name="components",
        null=True,
        blank=True,
    )
    type = models.CharField(
        "type",
        max_length=50,
        choices=ComponentTypes.choices,
        null=True,
        blank=True,
        default=None,
    )
    lifecycle = models.CharField(
        "lifecycle",
        max_length=50,
        choices=LifecycleTypes.choices,
        null=True,
        blank=True,
        default=None,
    )
    system = models.ForeignKey(
        System,
        on_delete=models.DO_NOTHING,
        verbose_name="system",
        related_name="components",
        null=True,
        blank=True,
    )
    context_level = models.CharField(
        "context level",
        max_length=50,
        choices=ContextLevel.choices,
        null=True,
        blank=True,
        default=None,
    )
    macroarea = models.ForeignKey(
        Macroarea,
        on_delete=models.DO_NOTHING,
        verbose_name="macroarea",
        related_name="components",
        null=True,
        blank=True,
    )

    critical = models.BooleanField("critical", default=False)
    cicd_url = models.URLField("custom ci/cd url", blank=True, null=True)
    is_filled = models.BooleanField("infos up to date", default=False)
    components = models.ManyToManyField("component", blank=True)
    api_doc_url = models.URLField("api doc url", blank=True, null=True)
    public_api_doc_url = models.URLField("public api doc url", blank=True, null=True)

    resources = models.ManyToManyField(
        Resource, verbose_name="resources", related_name="compoments", blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Automatically set the component's 'is_filled' field to True if all
        required fields are present.
        """
        if self.is_complete:
            self.is_filled = True
        else:
            self.is_filled = False

        super(Component, self).save(*args, **kwargs)

    @property
    def is_complete(self):
        """
        Check if the component has all required fields.
        """
        return (
            self.type is not None
            and self.lifecycle is not None
            and (self.macroarea is not None or self.group_owner is not None)
        )
