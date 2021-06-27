from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.permissions import AllowAny

from library.views import PublisherViewSet, WriterViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'publishers', PublisherViewSet)
router.register(r'writers', WriterViewSet)
router.register(r'books', BookViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="SeprisTestLibrary's API",
        default_version='v1',
        description="Sepris Library backend apis",
        terms_of_service="https://www.google.com/policies/terms/"
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
]
