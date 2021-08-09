from django.urls import path

from escape_rooms.accounts_app.views import UserRegisterView, UserUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('profile/', UserUpdateView.as_view()),
]
