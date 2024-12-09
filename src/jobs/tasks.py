import logging

from catalog.controllers.component_controller import (
    calculate_app_climate_score_for_components,
    create_or_update_app_climate_for_components,
    create_or_update_components_from_github,
)
from .celery import app

logger = logging.getLogger(__name__)

TASK_PING = "tasks.ping"
TASK_GITHUB = "tasks.import_github_repos"
TASK_APPCLIMATE = "tasks.manage_app_climate"
TASK_APPCLIMATE_SCORE = "tasks.calculate_app_climate_score"


@app.task
def ping(name=TASK_PING):
    logger.info("service is up by %s", name)


@app.task
def import_github_repos(name=TASK_GITHUB):
    logger.info("Starting %s", name)
    create_or_update_components_from_github()
    logger.info("Finished %s", name)


@app.task
def manage_app_climate(name=TASK_APPCLIMATE):
    logger.info("Starting %s", name)
    create_or_update_app_climate_for_components()
    logger.info("Finished %s", name)


@app.task
def calculate_app_climate_score(name=TASK_APPCLIMATE_SCORE):
    logger.info("Starting %s", name)
    calculate_app_climate_score_for_components()
    logger.info("Finished %s", name)
