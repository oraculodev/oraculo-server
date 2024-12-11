from .settings import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_DATABASE"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": int(env("DB_PORT")),
    }
}

CORS_ORIGIN_WHITELIST = ("https://oraculodev.com", "https://oraculodev.netlify.app")

RENDER_EXTERNAL_HOSTNAME = env("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME]
