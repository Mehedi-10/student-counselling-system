from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from scs.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="API for managing users",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),

]
