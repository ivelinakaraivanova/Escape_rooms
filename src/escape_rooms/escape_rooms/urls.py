"""escape_rooms URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from escape_rooms.escape_rooms_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('escape_rooms.accounts_app.urls')),   # TODO --> api/v1/
    path('escape/', include('escape_rooms.escape_rooms_app.urls')),
    path('companies/', include('escape_rooms.companies_app.urls')),
]
