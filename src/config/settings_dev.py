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

CORS_ORIGIN_WHITELIST = (
    "http://localhost:8080",
    "http://localhost:8081",
    "https://dev-oraculo.pesoreal.xyz",
    "https://release-oraculo.pesoreal.xyz",
)
