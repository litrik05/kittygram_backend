from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

from cats.views import AchievementViewSet, CatViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Cats API",
      default_version='v1',
      description="Документация для приложения cats проекта Kittygram",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="admin@kittygram.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),  # Работа с пользователями
    path('api/', include('djoser.urls.authtoken')),  # Работа с токенами
]

urlpatterns += [
   path(
       'swagger<format>/',
       schema_view.without_ui(cache_timeout=0),
       name='schema-json'
    ),
   path(
       'swagger/',
       schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'
    ),
   path(
       'redoc/',
       schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)