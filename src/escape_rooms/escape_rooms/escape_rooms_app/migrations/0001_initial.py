# Generated by Django 3.2.5 on 2021-07-31 13:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('used_jokers_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('decors_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('puzzle_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('staff_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('story_rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('total_rate', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('crime', 'Crime'), ('fantasy', 'Fantasy')], max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('opening_date', models.DateField()),
                ('difficulty', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('min_players', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2)])),
                ('max_players', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(6)])),
                ('owner_company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='companies_app.company')),
            ],
        ),
    ]
