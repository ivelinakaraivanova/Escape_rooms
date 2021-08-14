from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.utils import timezone

from escape_rooms.accounts_app.models import User
from escape_rooms.escape_app.validators import validate_start_time
from escape_rooms.organizations_app.models import Company


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
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
    )
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    owner_company = models.ForeignKey(Company, on_delete=models.RESTRICT)
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

    max_players = models.PositiveIntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(6),
        ]
    )

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(max_players__gte=F('min_players')),
                name='check_room_min_max_players',
            ),
        ]

    def __str__(self):
        return f"{self.id} {self.name} - {self.city} - {self.owner_company}"


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    players = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField(
        validators=[
            validate_start_time,
            MinValueValidator(limit_value=timezone.now)
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['room', 'start_datetime'], name='reservation unique room start_datetime')
        ]

    def __str__(self):
        return f"{self.room} - {self.team}"


class Game(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game_date = models.DateField(
        validators=[
            MaxValueValidator(limit_value=date.today)
         ]
    )
    duration = models.DurationField()
    used_jokers_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.room} - {self.team} - {self.game_date}"


class Review(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
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
    total_rate = models.FloatField()

    def save(self, *args, **kwargs):
        self.total_rate = (self.decors_rate + self.puzzle_rate + self.staff_rate + self.story_rate) / 4
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.room} - {self.content} - {self.total_rate}"
