from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.authtoken.admin import User

from escape_rooms.companies_app.models import Company


class Room(models.Model):
    TYPE_CHOICE_ACTION = 'action'
    TYPE_CHOICE_ADVENTURE = 'adventure'
    TYPE_CHOICE_CRIME = 'crime'
    TYPE_CHOICE_FANTASY = 'fantasy'

    TYPE_CHOICES = (
        (TYPE_CHOICE_ACTION, 'Action'),
        (TYPE_CHOICE_ADVENTURE, 'Adventure'),
        (TYPE_CHOICE_CRIME, 'Crime'),
        (TYPE_CHOICE_FANTASY, 'Fantasy'),

    )
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    opening_date = models.DateField()
    difficulty = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6),
        ]
    )
    min_players = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2),
        ]
    )
    # TODO --> test validation min_players <= max_players
    max_players = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(6),
        ]
    )
    owner_company = models.ForeignKey(Company, on_delete=models.RESTRICT)


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)
    players = models.ManyToManyField(User)


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    datetime = models.DateTimeField()  # TODO  --> validator for even hours - from-to; validator for free hours;
    # TODO --> unique room-datetime combination


class Game(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    datetime = models.DateTimeField()  # TODO  --> unique room-datetime combination; rename to start_datetime
    duration = models.DurationField()
    used_jokers_count = models.PositiveIntegerField(default=0)


class Review(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()
    decors_rate = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    puzzle_rate = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    staff_rate = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    story_rate = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )
    total_rate = models.PositiveIntegerField()  # TODO--> how to make calculated field