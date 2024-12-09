import logging

from django.conf import settings
from django.db.models import Count, F, Q

from catalog.models import AppClimateItem, Component, ComponentAppClimate
from catalog.models.app_climate_score import AppClimateScore, CalculateAppClimateScore
from catalog.models.component_app_climate_score import ComponentAppClimateScore
from catalog.models.group import Group
from core.services.github_service import GithubService
from core.utils.check_arguments import (
    check_argument_is_not_none,
)
from catalog.shared.choices import LifecycleTypes

logger = logging.getLogger(__name__)


def create_or_update_components_from_github():
    logger.debug("running...")

    github_service = GithubService(
        org=settings.GITHUB["ORG"], api_token=settings.GITHUB["API_KEY"]
    )

    repos = github_service.get_all_repos()

    count_added = 0
    for repo in repos:

        repo_data = {
            "name": repo["name"],
            "description": repo["description"],
            "repo_url": repo["html_url"],
            "repo_created_at": repo["created_at"],
            "repo_updated_at": repo["updated_at"],
            "repo_pushed_at": repo["pushed_at"],
        }
        if repo["archived"] is True:
            repo_data["lifecycle"] = LifecycleTypes.DEPRECATED

        component, created = Component.objects.update_or_create(
            repo_id=repo["id"],
            defaults=repo_data,
        )

        if repo["language"]:
            component.tags.add(repo["language"])

        if created:
            count_added += 1

    logger.debug(f"Services added: {count_added}")


def create_or_update_app_climate_for_components():
    logger.debug("running...")

    components = Component.objects.filter(
        Q(lifecycle=LifecycleTypes.PRODUCTION) | Q(is_filled=True)
    )
    app_climate_items = AppClimateItem.objects.all()

    for component in components:
        for item in app_climate_items:
            ComponentAppClimate.objects.update_or_create(
                component=component,
                app_climate_item=item,
            )


def create_or_update_component_app_climate_scores(
    component: Component, scores: CalculateAppClimateScore
):
    check_argument_is_not_none(component, "component")
    check_argument_is_not_none(scores, "scores")

    for _ in scores:
        # print(_.get_score())
        ComponentAppClimateScore.objects.update_or_create(
            component=component,
            app_climate_score=_.app_climate_score,
            defaults={"score": _.get_score()},
        )
        _.reset()


def calculate_app_climate_score_for_components(component=None):
    logger.debug("running...")

    if component:
        components_app_climate = ComponentAppClimate.objects.filter(
            component_id=component.id
        ).order_by("component", "app_climate_item__category")
        print(components_app_climate)
    else:
        components_app_climate = ComponentAppClimate.objects.all().order_by(
            "component", "app_climate_item__category"
        )

    app_climate_scores = AppClimateScore.objects.prefetch_related(
        "categories",
    ).all()

    if len(components_app_climate) == 0 or len(app_climate_scores) == 0:
        return

    calculate_app_climate_scores = []
    for app_climate_score in app_climate_scores:
        calculate_app_climate_scores.append(CalculateAppClimateScore(app_climate_score))

    _cp = components_app_climate[0].component
    for cac in components_app_climate:
        # print(cac.component.id, cac)
        if _cp != cac.component:
            create_or_update_component_app_climate_scores(
                _cp, calculate_app_climate_scores
            )
            _cp = cac.component

        for _ in calculate_app_climate_scores:
            if cac.app_climate_item.category in _.app_climate_score.categories.all():
                if cac.not_apply:
                    continue

                _.components_count += 1
                if cac.is_check:
                    _.components_checked_count += 1

    create_or_update_component_app_climate_scores(_cp, calculate_app_climate_scores)


def get_dashboard_data():
    production_services_count = Component.objects.filter(
        lifecycle=LifecycleTypes.PRODUCTION
    ).count()

    critical_services_count = Component.objects.filter(
        lifecycle=LifecycleTypes.PRODUCTION, critical=True
    ).count()

    not_up_to_date_services_count = Component.objects.filter(
        lifecycle=LifecycleTypes.PRODUCTION, is_filled=False
    ).count()

    services_by_group = (
        Group.objects.values("id", "name")
        .annotate(
            count=Count(
                "components",
                filter=Q(
                    components__lifecycle=LifecycleTypes.PRODUCTION,
                ),
            ),
        )
        .filter(
            is_active=True,
            count__gt=0,
        )
        .order_by("name")
    )

    services_count_by_type = (
        Component.objects.values("type")
        .annotate(count=Count("type"))
        .exclude(type__isnull=True)
        .filter(
            lifecycle=LifecycleTypes.PRODUCTION,
        )
        .order_by("type")
    )

    services_count_by_macroarea = (
        Component.objects.values("macroarea__name")
        .annotate(count=Count("macroarea"))
        .exclude(macroarea__isnull=True)
        .filter(
            lifecycle=LifecycleTypes.PRODUCTION,
        )
        .order_by("macroarea__name")
    )

    data = {
        "production_services_count": production_services_count,
        "critical_services_count": critical_services_count,
        "not_up_to_date_services_count": not_up_to_date_services_count,
        "services_by_group": services_by_group,
        "services_count_by_type": services_count_by_type,
        "services_count_by_macroarea": services_count_by_macroarea,
    }

    return [data]
