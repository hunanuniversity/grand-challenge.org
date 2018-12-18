from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.authtoken import views
from .views import IndexView, ThumbnailView, NumpyView
from django.views.decorators.cache import cache_page
from django.conf import settings


app_name = "retina"
urlpatterns = [
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("", IndexView.as_view(), name="home"),
    path("api/", include("grandchallenge.retina_api.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    path("archives/", include("grandchallenge.archives.urls")),
    path("patients/", include("grandchallenge.patients.urls")),
    path("studies/", include("grandchallenge.studies.urls")),
    # path("retina_images/", include("grandchallenge.retina_images.urls")),
    path("annotations/", include("grandchallenge.annotations.urls")),
    path("retina_importers/", include("grandchallenge.retina_importers.urls")),
    path("registrations/", include("grandchallenge.registrations.urls")),
    path(
        "image/thumbnail/<uuid:image_id>/",
        cache_page(settings.RETINA_IMAGE_CACHE_TIME)(ThumbnailView.as_view()),
        name="image-thumbnail",
    ),
    path(
        "image/numpy/<uuid:image_id>/",
        cache_page(settings.RETINA_IMAGE_CACHE_TIME)(NumpyView.as_view()),
        name="image-numpy",
    ),
]