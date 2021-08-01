from rest_framework import serializers
from rest_framework.authtoken.admin import User

from escape_rooms.escape_rooms_app.models import Room, Team, Game, Reservation, Review


class UserNameSerializer(serializers.ModelSerializer):  # TODO --> to move to accounts
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class RoomListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        depth = 1   # TODO --> nested serializers after more fields in company


class RoomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def validate(self, data):  # TODO --> write test; check constraint
        if data['min_players'] > data['max_players']:
            raise serializers.ValidationError('Minimum players cannot be bigger than maximum players')
        return data


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
        fields = ('id', 'room', 'team', 'datetime')


class ReservationCreateUpdateSerializer(serializers.ModelSerializer):
    # room = serializers.PrimaryKeyRelatedField(
    #     queryset=Room.objects.all())
    # team = serializers.PrimaryKeyRelatedField(
    #     queryset=Team.objects.all())

    class Meta:
        model = Reservation
        fields = '__all__'


class GameListDetailSerializer(serializers.ModelSerializer):
    room = RoomShortSerializer()
    team = TeamListSerializer()

    class Meta:
        model = Game
        fields = ('id', 'room', 'team', 'datetime', 'duration', 'used_jokers_count')


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
        fields = '__all__'
