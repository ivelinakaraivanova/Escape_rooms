# Generated by Django 3.2.5 on 2021-08-13 17:39

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.utils.timezone
import escape_rooms.escape_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('crime', 'Crime'), ('fantasy', 'Fantasy')], max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('opening_date', models.DateField()),
                ('difficulty', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('min_players', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2)])),
                ('max_players', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(6)])),
                ('owner_company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='organizations_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('decors_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('puzzle_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('staff_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('story_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('total_rate', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escape_app.room')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(validators=[escape_rooms.escape_app.validators.validate_start_time, django.core.validators.MinValueValidator(limit_value=django.utils.timezone.now)])),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escape_app.room')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escape_app.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)])),
                ('duration', models.DurationField()),
                ('used_jokers_count', models.PositiveIntegerField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escape_app.room')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escape_app.team')),
            ],
        ),
        migrations.AddConstraint(
            model_name='room',
            constraint=models.CheckConstraint(check=models.Q(('max_players__gte', django.db.models.expressions.F('min_players'))), name='check_room_min_max_players'),
        ),
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.UniqueConstraint(fields=('room', 'start_datetime'), name='reservation unique room start_datetime'),
        ),
    ]
