from csvexport.actions import csvexport
from django.contrib import admin
from django.utils.html import format_html
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from catalog.controllers.component_controller import (
    calculate_app_climate_score_for_components,
)
from catalog.models import (
    AppClimateCategory,
    AppClimateItem,
    AppClimateScore,
    Component,
    ComponentAppClimate,
    ComponentAppClimateScore,
    ComponentGroupLink,
    ComponentLink,
    ComponentNote,
    Group,
    GroupGroupLink,
    GroupLink,
    GroupNote,
    Link,
    Macroarea,
    Member,
    Resource,
    ResourceType,
    Role,
    System,
    SystemGroupLink,
    SystemLink,
)


###
# COMPONENT
###
class ComponentAppClimateInline(NestedStackedInline):
    model = ComponentAppClimate
    readonly_fields = ["item_doc_url"]
    ordering = ("app_climate_item__category",)
    extra = 0

    def item_doc_url(self, obj):
        return format_html(
            "<a href='{url}' target='_blank'>{url}</a>", url=obj.item_doc_url()
        )


class ComponentLinkInline(NestedStackedInline):
    model = ComponentLink
    extra = 1


class ComponentGroupLinkInline(NestedStackedInline):
    model = ComponentGroupLink
    extra = 1
    inlines = [ComponentLinkInline]


class ComponentNoteInline(NestedStackedInline):
    model = ComponentNote
    extra = 0


@admin.register(Component)
class ComponentAdmin(NestedModelAdmin):
    actions = [csvexport]
    filter_horizontal = ("components", "resources")
    inlines = [
        ComponentGroupLinkInline,
        ComponentAppClimateInline,
        ComponentNoteInline,
    ]

    ordering = ("name",)

    list_display = [
        "name",
        "custom_repo_url",
        "macroarea",
        "group_owner",
        "type",
        "lifecycle",
        "context_level",
        "critical",
        "custom_tags",
        "is_filled",
    ]
    list_filter = [
        "type",
        "lifecycle",
        "tags",
        "group_owner",
        "system",
        "critical",
        "is_filled",
        "context_level",
    ]
    search_fields = [
        "name",
    ]
    fieldsets = (
        (
            "STANDARD INFOS",
            {
                "fields": (
                    "name",
                    "repo_id",
                    "repo_url",
                    "description",
                    "type",
                    "lifecycle",
                    "macroarea",
                    "group_owner",
                    "context_level",
                    "system",
                    "critical",
                    "tags",
                    "cicd_url",
                    "api_doc_url",
                    "public_api_doc_url",
                    "created_at",
                    "updated_at",
                )
            },
        ),
        (
            "Recursos utilizados",
            {"fields": ("resources",)},
        ),
        (
            "Dependência de componentes",
            {"fields": ("components",)},
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["created_at",
                    "updated_at",
                    "repo_id",]
        else:
            return ["created_at",
                    "updated_at",]

    def custom_tags(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    custom_tags.short_description = "tags"

    def custom_repo_url(self, obj):
        return format_html("<a href='{url}' target='blank'>{url}</a>", url=obj.repo_url)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "group_owner":
            kwargs["queryset"] = Group.objects.order_by("name")
        elif db_field.name == "system":
            kwargs["queryset"] = System.objects.order_by("name")
        return super(ComponentAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def response_add(self, request, new_object):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(ComponentAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(ComponentAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, obj):
        calculate_app_climate_score_for_components(obj)
        return obj


###
# RESOURCE
###
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    actions = [csvexport]
    ordering = ("name",)

    list_display = [
        "name",
        "type",
        "lifecycle",
        "created_at",
    ]

    list_filter = [
        "lifecycle",
        "type",
    ]

    search_fields = [
        "name",
    ]


###
# RESOURCE TYPES
###
@admin.register(ResourceType)
class ResourceTypesAdmin(admin.ModelAdmin):
    actions = [csvexport]
    ordering = ("name",)

    list_display = [
        "name",
        "created_at",
    ]


###
# GROUP
###
class GroupLinkInline(NestedStackedInline):
    model = GroupLink
    extra = 1


class GroupGroupLinkInline(NestedStackedInline):
    model = GroupGroupLink
    extra = 1
    inlines = [GroupLinkInline]


class GroupNoteInline(NestedStackedInline):
    model = GroupNote
    extra = 0


@admin.register(Group)
class GroupAdmin(NestedModelAdmin):
    actions = [csvexport]
    filter_horizontal = (
        "members",
        "other_components",
    )
    inlines = [
        GroupGroupLinkInline,
        GroupNoteInline,
    ]
    ordering = ("name",)

    list_display = [
        "name",
        "description",
        "parent",
        "type",
        "is_active",
    ]

    list_filter = [
        "is_active",
        "type",
        "parent",
    ]

    search_fields = [
        "name",
    ]

    fieldsets = (
        (
            "STANDARD INFOS",
            {
                "fields": (
                    "name",
                    "description",
                    "is_active",
                    "type",
                    "parent",
                    "tags",
                    "board_url",
                    "design_url",
                    "members",
                    "other_components",
                )
            },
        ),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Group.objects.order_by("name")
        return super(GroupAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


###
# SYSTEM
###
class SystemLinkInline(NestedStackedInline):
    model = SystemLink
    extra = 1


class SystemGroupLinkInline(NestedStackedInline):
    model = SystemGroupLink
    extra = 1
    inlines = [SystemLinkInline]


@admin.register(System)
class SystemAdmin(NestedModelAdmin):
    actions = [csvexport]
    filter_horizontal = ("groups",)
    inlines = [SystemGroupLinkInline]
    ordering = ("name",)

    list_display = [
        "name",
        "custom_tags",
        "custom_groups",
        "lifecycle",
        "description",
        "created_at",
    ]

    list_filter = [
        "lifecycle",
        "tags",
        "groups",
    ]

    def custom_tags(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    custom_tags.short_description = "tags"

    def custom_groups(self, obj):
        return ", ".join(o.name for o in obj.groups.all())

    custom_groups.short_description = "groups"


###
# MACROAREA
###
@admin.register(Macroarea)
class MacroAdmin(admin.ModelAdmin):
    actions = [csvexport]
    ordering = ("name",)

    list_display = [
        "name",
        "created_at",
    ]


###
# MEMBER
###
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    actions = [csvexport]
    ordering = ("name",)

    list_display = [
        "name",
        "email",
        "role",
        "custom_tags",
        "created_at",
    ]

    list_filter = [
        "role",
    ]

    search_fields = [
        "name",
    ]

    def custom_tags(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    custom_tags.short_description = "tags"


###
# ROLES
###
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    actions = [csvexport]
    ordering = ("name",)

    list_display = [
        "name",
        "created_at",
    ]


###
# Link
###
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    actions = [csvexport]
    list_display = [
        "title",
        "description",
        "icon",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "title",
    ]


###
# App Climate
###
@admin.register(AppClimateCategory)
class AppClimateCategoryAdmin(admin.ModelAdmin):
    actions = [csvexport]
    list_display = [
        "name",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "name",
    ]

    ordering = ("name",)


@admin.register(AppClimateItem)
class AppClimateItemAdmin(admin.ModelAdmin):
    actions = [csvexport]
    list_display = [
        "name",
        "category",
        "doc_url",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "category",
    ]

    search_fields = [
        "name",
    ]

    ordering = (
        "category__name",
        "name",
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = AppClimateCategory.objects.order_by("name")
        return super(AppClimateItemAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


@admin.register(ComponentAppClimate)
class ComponentAppClimateAdmin(admin.ModelAdmin):
    actions = [csvexport]
    list_display = [
        "component",
        "get_group_owner_name",
        "get_category",
        "app_climate_item",
        "is_check",
        "not_apply",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "component__lifecycle",
        "is_check",
        "not_apply",
        "app_climate_item",
    ]

    ordering = (
        "component__name",
        "app_climate_item__category__name",
        "app_climate_item__name",
    )

    def get_group_owner_name(self, obj):
        return obj.component.group_owner.name if obj.component.group_owner else ""

    get_group_owner_name.short_description = "Owner"

    def get_category(self, obj):
        return obj.app_climate_item.category.name

    get_category.short_description = "Category"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "component":
            kwargs["queryset"] = Component.objects.order_by("name")
        return super(ComponentAppClimateAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


@admin.register(AppClimateScore)
class AppClimateScoreAdmin(admin.ModelAdmin):
    actions = [csvexport]
    filter_horizontal = ("categories",)

    list_display = [
        "name",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "name",
    ]

    ordering = ("name",)


@admin.register(ComponentAppClimateScore)
class ComponentAppClimateScoreAdmin(admin.ModelAdmin):
    actions = [csvexport]
    list_display = [
        "component",
        "get_group_owner_name",
        "get_score_name",
        "score",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "component__lifecycle",
        "component__critical",
        "component",
        "component__group_owner__name",
        "app_climate_score",
    ]

    ordering = (
        "component__name",
        "app_climate_score__name",
    )

    def get_group_owner_name(self, obj):
        return obj.component.group_owner.name if obj.component.group_owner else ""

    get_group_owner_name.short_description = "Owner"

    def get_score_name(self, obj):
        return obj.app_climate_score.name

    get_score_name.short_description = "Score name"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "component":
            kwargs["queryset"] = Component.objects.order_by("name")
        return super(ComponentAppClimateScoreAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
