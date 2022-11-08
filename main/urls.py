from django.contrib import admin

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from django.views.decorators.cache import cache_page

from account.views import auth

schema_view = get_schema_view(
   openapi.Info(
      title="Video hosting test project",
      default_version='v1',
      description="Test REST API backend at django",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = SimpleRouter()


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', cache_page(60)(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/', include('service.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)