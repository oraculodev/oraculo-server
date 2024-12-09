import datetime

from django.conf import settings
from django.db import connection
from django.http import JsonResponse


def HealthCheck(request):
    return JsonResponse({"message": "ok"})


def Status(request):
    updated_at = datetime.datetime.now().isoformat()

    with connection.cursor() as cursor:
        cursor.execute("SHOW server_version;")
        rows = cursor.fetchone()
        database_version_value = rows[0]

        cursor.execute("SHOW max_connections;")
        rows = cursor.fetchone()
        database_max_connection_value = rows[0]

        database_name = settings.DATABASES["default"]["NAME"]
        cursor.execute(
            "SELECT count(*)::int FROM pg_stat_activity WHERE datname = %s;",
            [database_name],
        )
        database_opened_connections_value = rows[0]

    return JsonResponse(
        {
            "updated_at": updated_at,
            "dependencies": {
                "database": {
                    "version": database_version_value,
                    "max_connections": int(database_max_connection_value),
                    "opened_connections": int(database_opened_connections_value),
                },
            },
        }
    )
