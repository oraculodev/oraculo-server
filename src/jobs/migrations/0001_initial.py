# Generated by Django 3.2.13 on 2022-07-18 12:50

from django.db import migrations
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask


def setup_schedulers(apps, schema_editor):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.MINUTES,
    )
    PeriodicTask.objects.create(
        interval=schedule,
        name='Ping',
        task='jobs.tasks.ping',
    )

    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='30',
        hour='7',
        day_of_week='1',
        day_of_month='*',
        month_of_year='*',
    )
    PeriodicTask.objects.create(
        crontab=schedule,
        name='Import Github',
        task='jobs.tasks.import_github_repos',
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(setup_schedulers),
    ]
