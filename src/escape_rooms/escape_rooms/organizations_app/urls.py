from django.urls import path

from escape_rooms.organizations_app.views import CompanyListView, CompanyDetailView, CompanyCreateView, \
    EmployeeListView, EmployeeDetailView, EmployeeCreateView

urlpatterns = [
    path('companies/', CompanyListView.as_view()),
    path('company/<int:pk>/', CompanyDetailView.as_view()),
    path('company/', CompanyCreateView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('employee/<int:pk>/', EmployeeDetailView.as_view()),
    path('employee/', EmployeeCreateView.as_view()),
]