"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from atexit import register

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from catalog.routes.components import (
    ComponentAppClimateScoreViewSet,
    ComponentAppClimateViewSet,
    ComponentViewSet,
)
from catalog.routes.dash import DashViewSet
from catalog.routes.groups import GroupViewSet
from catalog.routes.links import LinkViewSet
from catalog.routes.systems import SystemViewSet
from core.routes import HealthCheck, Status

api_router = DefaultRouter()
api_router.register(r"components", ComponentViewSet).register(
    r"appclimate",
    ComponentAppClimateViewSet,
    "component-appclimate",
    parents_query_lookups=["component_id"],
)
api_router.register(r"components", ComponentViewSet).register(
    r"appclimatescore",
    ComponentAppClimateScoreViewSet,
    "component-appclimatescore",
    parents_query_lookups=["component_id"],
)
api_router.register(r"groups", GroupViewSet)
api_router.register(r"systems", SystemViewSet)
api_router.register(r"links", LinkViewSet)
api_router.register(r"dash", DashViewSet, basename="dash")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_router.urls)),
    path("healthcheck", HealthCheck),
    path("status", Status),
    path("tinymce/", include("tinymce.urls")),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
