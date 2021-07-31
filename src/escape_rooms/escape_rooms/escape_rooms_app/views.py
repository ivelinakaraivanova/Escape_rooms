from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         content = {
#             'message': 'Hello World!',
#         }
#         return Response(content)

from escape_rooms.escape_rooms_app.models import Room, Team, Game, Reservation, Review
from escape_rooms.escape_rooms_app.serializers import RoomSerializer, GameSerializer, \
    ReservationSerializer, ReviewSerializer, TeamListSerializer, TeamDetailSerializer, TeamCreateUpdateSerializer


class RoomListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCreateView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TeamListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer


class TeamCreateView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateUpdateSerializer


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return TeamDetailSerializer
        else:
            return TeamCreateUpdateSerializer


class ReservationListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationCreateView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class GameListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameCreateView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ReviewListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
