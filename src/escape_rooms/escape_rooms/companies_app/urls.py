from django.urls import path

from escape_rooms.companies_app.views import CompanyListView, CompanyDetailView, CompanyCreateView

urlpatterns = [
    path('companies/', CompanyListView.as_view()),
    path('company/<int:pk>/', CompanyDetailView.as_view()),
    path('company/', CompanyCreateView.as_view()),
]
