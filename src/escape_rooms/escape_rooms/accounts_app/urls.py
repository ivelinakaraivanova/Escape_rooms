from django.urls import path, include

from escape_rooms.accounts_app.views import CompanyListView, CompanyDetailView, CompanyCreateView, EmployeeListView, \
    EmployeeDetailView, EmployeeCreateView, UserRegisterView, UserUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('profile/', UserUpdateView.as_view()),
    path('companies/', CompanyListView.as_view()),
    path('company/<int:pk>/', CompanyDetailView.as_view()),
    path('company/', CompanyCreateView.as_view()),
    path('employees/', EmployeeListView.as_view()),
    path('employee/<int:pk>/', EmployeeDetailView.as_view()),
    path('employee/', EmployeeCreateView.as_view()),
]