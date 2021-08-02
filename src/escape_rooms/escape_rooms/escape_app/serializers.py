from rest_framework import serializers
from rest_framework.authtoken.admin import User

from escape_rooms.escape_app.models import Room, Team, Game, Reservation, Review, Company


class UserNameSerializer(serializers.ModelSerializer):  # TODO --> to move to accounts
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class RoomListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        depth = 1   # TODO --> nested serializers after making more fields in company


class RoomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'city')


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class TeamDetailSerializer(serializers.ModelSerializer):
    players = UserNameSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'players')


class TeamCreateUpdateSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())

    class Meta:
        model = Team
        fields = ('id', 'name', 'players')


class ReservationListDetailSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer()
    team = TeamListSerializer()

    class Meta:
        model = Reservation
        fields = ('id', 'room', 'team', 'start_datetime')


class ReservationCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


class GameListDetailSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer()
    team = TeamListSerializer()

    class Meta:
        model = Game
        fields = ('id', 'room', 'team', 'start_datetime', 'duration', 'used_jokers_count')


class GameCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer()
    player = UserNameSerializer()

    class Meta:
        model = Review
        fields = ('id', 'room', 'player', 'date', 'content', 'total_rate')


class ReviewDetailSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer()
    player = UserNameSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('total_rate',)
