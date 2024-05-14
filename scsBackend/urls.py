from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

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

    path('universities/', university_list, name='university-list'),
    path('universities/<int:pk>/', university_detail_get, name='university-detail-get'),
    path('universities/<int:pk>/modify/', university_detail_modify, name='university-detail-modify'),
    path('universities/new/', university_create, name='university-create'),

    path('colleges/', college_list, name='college-list'),
    path('colleges/<int:pk>/', college_detail_get, name='college-detail-get'),
    path('colleges/<int:pk>/modify/', college_detail_modify, name='college-detail-modify'),
    path('colleges/new/', college_create, name='college-create'),

    path('campuses/', campus_list, name='campus-list'),
    path('campuses/<int:pk>/', campus_detail_get, name='campus-detail-get'),
    path('campuses/<int:pk>/modify/', campus_detail_modify, name='campus-detail-modify'),
    path('campuses/new/', campus_create, name='campus-create'),

    path('departments/', department_list, name='department-list'),
    path('departments/<int:pk>/', department_detail_get, name='department-detail-get'),
    path('departments/<int:pk>/modify/', department_detail_modify, name='department-detail-modify'),
    path('departments/new/', department_create, name='department-create'),

    path('faculty-members/', faculty_member_list, name='faculty-member-list'),
    path('faculty-members/<int:pk>/', faculty_member_detail_get, name='faculty-member-detail-get'),
    path('faculty-members/<int:pk>/modify/', faculty_member_detail_modify, name='faculty-member-detail-modify'),
    path('facultys/new/', faculty_create, name='faculty-create'),

    path('fundings/', funding_list, name='funding-list'),
    path('fundings/<int:pk>/', funding_detail_get, name='funding-detail-get'),
    path('fundings/<int:pk>/modify/', funding_detail_modify, name='funding-detail-modify'),
    path('fundings/new/', funding_create, name='funding-create'),

    path('biographic-information/', biographic_information, name='biographic-information'),

]
