from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Bookshelf API",
        default_version='v1',
        description="description for bookshelf API",
        terms_of_service="google.com",
        contact=openapi.Contact(email="helloshohjahon@gmail.com"),
        license=openapi.License(name="None")
    ),
    public=True, permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('books/', include('apps.books.urls')),
    
    #   swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
