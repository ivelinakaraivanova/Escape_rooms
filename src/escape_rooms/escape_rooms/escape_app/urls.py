from django.urls import path

from escape_rooms.escape_app.views import *
    # RoomCreateView, RoomDetailView, RoomListView, TeamListView, \
    # TeamCreateView, TeamDetailView, GameListView, GameDetailView, GameCreateView, ReservationListView, \
    # ReservationDetailView, ReservationCreateView, ReviewListView, ReviewDetailView, ReviewCreateView


class ReservationTeamDetailView:
    pass


urlpatterns = [
    path('rooms/', RoomListView.as_view()),
    path('room/<int:pk>/', RoomDetailView.as_view()),
    path('room/', RoomCreateView.as_view()),
    path('teams/', TeamListView.as_view()),
    path('team/<int:pk>/', TeamDetailView.as_view()),
    path('team/', TeamCreateView.as_view()),
    path('games/', GameListView.as_view()),
    path('game/<int:pk>/', GameDetailView.as_view()),
    path('game/', GameCreateView.as_view()),
    path('reservations/', ReservationListView.as_view()),
    path('reservation/<int:pk>/', ReservationDetailView.as_view()),
    path('reservation/', ReservationCreateView.as_view()),
    path('reviews/', ReviewListView.as_view()),
    path('review/<int:pk>/', ReviewDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),
]