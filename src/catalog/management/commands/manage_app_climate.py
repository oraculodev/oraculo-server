import logging

from django.core.management.base import BaseCommand

from catalog.controllers.component_controller import (
    create_or_update_app_climate_for_components,
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Update App Climate for Components"

    def handle(self, *args, **options):

        logger.info("Command BEGIN [%s]", self.help)

        create_or_update_app_climate_for_components()

        logger.info("Command END [%s]", self.help)
