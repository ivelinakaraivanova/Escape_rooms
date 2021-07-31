from rest_framework import serializers
from rest_framework.authtoken.admin import User

from escape_rooms.escape_rooms_app.models import Room, Team, Game, Reservation, Review


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def validate(self, data):   # TODO --> write test
        if data['min_players'] > data['max_players']:
            raise serializers.ValidationError('Minimum players cannot be bigger than maximum players')
        return data

# class RoomListSerializer(serializers.ModelSerializer):


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class TeamDetailSerializer(serializers.ModelSerializer):
    players = UserNameSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'players')
        depth = 1


class TeamCreateUpdateSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())

    class Meta:
        model = Team
        fields = ('id', 'name', 'players')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
