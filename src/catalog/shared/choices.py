from django.db import models


class LifecycleTypes(models.TextChoices):
    DEPRECATED = "deprecated"
    EXPERIMENTAL = "experimental"
    PRODUCTION = "production"


class ComponentTypes(models.TextChoices):
    APP = "app"
    API = "api"
    DOCS = "docs"
    LIBRARY = "library"
    SERVICE = "service"
    WEBSITE = "website"


class GroupTypes(models.TextChoices):
    CHAPTER = "chapter"
    DEPARTMENT = "department"
    ORGANIZATION = "organization"
    TEAM = "team"
    TRIBE = "tribe"


class ContextLevel(models.TextChoices):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
