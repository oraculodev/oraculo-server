import logging

from django.core.management.base import BaseCommand

from catalog.controllers.component_controller import (
    create_or_update_components_from_github,
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import repositories from Github"

    def handle(self, *args, **options):

        logger.info("Command BEGIN [%s]", self.help)

        create_or_update_components_from_github()

        logger.info("Command END [%s]", self.help)
