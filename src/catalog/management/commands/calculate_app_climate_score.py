import logging

from django.core.management.base import BaseCommand

from catalog.controllers.component_controller import (
    calculate_app_climate_score_for_components,
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Calculate App Climate Score for Components"

    def handle(self, *args, **options):

        logger.info("Command BEGIN [%s]", self.help)

        calculate_app_climate_score_for_components()

        logger.info("Command END [%s]", self.help)
