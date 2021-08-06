from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from escape_rooms.escape_app.models import Room, Team, Game, Reservation, Review
from escape_rooms.escape_app.permissions import IsOwnerCompanyEmployeeOrReadOnly, IsMemberOrReadOnly, \
    IsTeamMemberOrRoomOwnerCompanyEmployeeOrReadOnly, IsRoomOwnerCompanyEmployeeOrReadOnly, IsUserReviewOrReadOnly
from escape_rooms.escape_app.serializers import RoomCreateUpdateSerializer, GameCreateUpdateSerializer, \
    ReviewCreateUpdateSerializer, TeamListSerializer, TeamDetailSerializer, TeamCreateUpdateSerializer, \
    ReservationListDetailSerializer, GameListDetailSerializer, ReviewListSerializer, ReservationCreateUpdateSerializer, \
    ReviewDetailSerializer, RoomListDetailSerializer


class RoomListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Room.objects.all()
    serializer_class = RoomListDetailSerializer


class RoomCreateView(CreateAPIView):
    permission_classes = (IsOwnerCompanyEmployeeOrReadOnly,)
    queryset = Room.objects.all()
    serializer_class = RoomCreateUpdateSerializer


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerCompanyEmployeeOrReadOnly,)
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return RoomListDetailSerializer
        else:
            return RoomCreateUpdateSerializer


class TeamListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer


class TeamCreateView(CreateAPIView):
    permission_classes = (IsMemberOrReadOnly,)
    queryset = Team.objects.all()
    serializer_class = TeamCreateUpdateSerializer


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsMemberOrReadOnly,)
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return TeamDetailSerializer
        else:
            return TeamCreateUpdateSerializer


class ReservationListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationListDetailSerializer


class ReservationCreateView(CreateAPIView):
    permission_classes = (IsTeamMemberOrRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationCreateUpdateSerializer


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTeamMemberOrRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Reservation.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return ReservationListDetailSerializer
        else:
            return ReservationCreateUpdateSerializer


class GameListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Game.objects.all()
    serializer_class = GameListDetailSerializer


class GameCreateView(CreateAPIView):
    permission_classes = (IsRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameCreateUpdateSerializer


class GameDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Game.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return GameListDetailSerializer
        else:
            return GameCreateUpdateSerializer


class ReviewListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class ReviewCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserReviewOrReadOnly,)
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return ReviewDetailSerializer
        else:
            return ReviewCreateUpdateSerializer
