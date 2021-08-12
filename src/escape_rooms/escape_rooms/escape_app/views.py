from django.db.models import Count, Avg
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
    """
    Returns a list of all escape rooms.
    No authentication required.
    Optional filtering, searching, ordering and pagination.
    """
    permission_classes = (AllowAny,)
    queryset = Room.objects.annotate(review_count=Count('review'), average_total_rate=Avg('review__total_rate'))
    serializer_class = RoomListDetailSerializer
    filterset_fields = {
        'city': ['exact'],
        'category': ['exact'],
        'owner_company': ['exact'],
        'address': ['contains'],
        'difficulty': ['exact', 'gte', 'gt', 'lte', 'lt'],
    }
    search_fields = ['name', 'description', 'owner_company__name', 'city', 'address']
    ordering_fields = '__all__'


class RoomCreateView(CreateAPIView):
    """
    Create an escape room.
    Allowed for an employee of escape room's company and superuser only.
    """
    permission_classes = (IsOwnerCompanyEmployeeOrReadOnly,)
    queryset = Room.objects.all()
    serializer_class = RoomCreateUpdateSerializer


class RoomDetailView(RetrieveUpdateDestroyAPIView):
    """
    Read, update or delete an escape room.
    Allowed for an employee of escape room's company and superuser only.
    """
    permission_classes = (IsOwnerCompanyEmployeeOrReadOnly,)
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return RoomListDetailSerializer
        else:
            return RoomCreateUpdateSerializer


class TeamListView(ListAPIView):
    """
    Returns a list of all teams.
    No authentication required.
    Optional filtering, searching, ordering and pagination.
    """
    permission_classes = (AllowAny,)
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
    filterset_fields = ['players__id']
    search_fields = ['name']
    ordering_fields = '__all__'


class TeamCreateView(CreateAPIView):
    """
    Create a team.
    Allowed for a member of the created team and superuser only.
    """
    permission_classes = (IsMemberOrReadOnly,)
    queryset = Team.objects.all()
    serializer_class = TeamCreateUpdateSerializer


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    """
    Read, update or delete a team.
    Allowed for a team member and superuser only.
    """
    permission_classes = (IsMemberOrReadOnly,)
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return TeamDetailSerializer
        else:
            return TeamCreateUpdateSerializer


class ReservationListView(ListAPIView):
    """
    Returns a list of all reservations made.
    No authentication required.
    Optional filtering, ordering and pagination.
    """
    permission_classes = (AllowAny,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationListDetailSerializer
    filterset_fields = {
        'room': ['exact'],
        'team': ['exact'],
        'start_datetime': ['exact', 'gte', 'gt', 'lte', 'lt',
                           'date', 'date__gte',  'date__gt',
                           'date__lte', 'date__lt']
    }
    # search_fields = [] no search needed
    ordering_fields = ['room__name', 'team__name', 'start_datetime']


class ReservationCreateView(CreateAPIView):
    """
    Create a game reservation.
    Allowed for a team member, an employee of escape room's company or superuser.
    """
    permission_classes = (IsTeamMemberOrRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationCreateUpdateSerializer


class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    """
    Read, update or delete a game reservation.
    Allowed for a team member, an employee of escape room's company or superuser.
    """
    permission_classes = (IsTeamMemberOrRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Reservation.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return ReservationListDetailSerializer
        else:
            return ReservationCreateUpdateSerializer


class GameListView(ListAPIView):
    """
    Returns a list of all records for games played.
    No authentication required.
    Optional filtering, ordering and pagination.
    """
    permission_classes = (AllowAny,)
    queryset = Game.objects.all()
    serializer_class = GameListDetailSerializer
    filterset_fields = {
        'room': ['exact'],
        'team': ['exact'],
        'game_date': ['exact', 'gte', 'gt', 'lte', 'lt']
    }
    # search_fields = [] no search needed
    ordering_fields = ['room__name', 'team__name', 'game_date']


class GameCreateView(CreateAPIView):
    """
    Create a record for a game played.
    Allowed for an employee of escape room's company and superuser only.
    """
    permission_classes = (IsRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameCreateUpdateSerializer


class GameDetailView(RetrieveUpdateDestroyAPIView):
    """
    Read, update or delete a record for a game played.
    Allowed for an employee of escape room's company and superuser only.
    """
    permission_classes = (IsRoomOwnerCompanyEmployeeOrReadOnly,)
    queryset = Game.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return GameListDetailSerializer
        else:
            return GameCreateUpdateSerializer


class ReviewListView(ListAPIView):
    """
    Returns a list of all reviews written.
    No authentication required.
    Optional filtering, searching, ordering and pagination.
    """
    permission_classes = (AllowAny,)
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    filterset_fields = {
        'player': ['exact'],
        'room': ['exact'],
        'date': ['exact', 'gte', 'gt', 'lte', 'lt'],
        'content': ['contains'],
        'total_rate': ['exact', 'gte', 'gt', 'lte', 'lt']
    }
    search_fields = ['content']
    ordering_fields = ['room__name', 'total_rate', 'date']


class ReviewCreateView(CreateAPIView):
    """
    Create a review.
    Allowed for authenticated user only.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    """
    Read, update or delete a review written.
    Allowed for the review writer and superuser only.
    """
    permission_classes = (IsUserReviewOrReadOnly,)
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return ReviewDetailSerializer
        else:
            return ReviewCreateUpdateSerializer
