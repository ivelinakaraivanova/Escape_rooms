from django.urls import path, include

from escape_rooms.accounts_app.views import CompanyListView, CompanyDetailView, CompanyCreateView

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('companies/', CompanyListView.as_view()),
    path('company/<int:pk>/', CompanyDetailView.as_view()),
    path('company/', CompanyCreateView.as_view()),
]