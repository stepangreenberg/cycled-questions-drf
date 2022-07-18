from django.contrib import admin
from django.urls import path, include
from cycled_questions import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Questions",
        default_version="1.0.0",
    )
)

urlpatterns = [
    path("", views.api_root, name="api_root"),
    path("yeild-question/<str:name>/", views.yield_question, name="yield_question"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    path("api/v1/cycled_questions/", include("cycled_questions.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
]
