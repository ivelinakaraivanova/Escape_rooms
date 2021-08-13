from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contrib-auth/', include('django.contrib.auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/v1/accounts/', include('escape_rooms.accounts_app.urls')),
    path('api/v1/escape/', include('escape_rooms.escape_app.urls')),
    path('api/v1/organizations/', include('escape_rooms.organizations_app.urls')),
]
