# Escape_rooms
With this project I experimented working with various aspects of the Django REST framework.

## The idea
The project presents a catalog of escape rooms and all activities related to the game in them. Its purpose is to enable fans to easily and conveniently navigate and choose the right entertainment.

## This is an API for:
*	accounts for players and escape room company employees
*	teams of players
*	escape rooms
*	making escape room reservations
*	keeping track of games played in escape rooms
*	reviews of escape rooms

## Built with
*	Python 3.9
*	Django REST framework
*	PostgreSQL

## Running Locally
1.	Must have Python 3 & PostgreSQL installed and running
2.	Clone the repo and cd into repo
3.	Create a virtual environment: `python -m venv venv`
4.	Go into your virtual environment: `source venv/bin/activate`
5.	Install dependencies: `pip install -r requirements.txt`
6.	Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`
7.	Setup Database
    *	Create the database: `CREATE DATABASE escaperooms`;
    *	Run migrations: `python manage.py migrate`
8.	Run the app: `python manage.py runserver`
9.	View the API at `localhost:8000 and the admin interface at localhost:8000/admin`


## Schema

* User
  * username
  * password
  * email
  * first_name
  * last_name

* Company (escape room owner)
  * name

* Employee (of an escape room company)
  * user
  * company

* Room (escape room)
  * name
  * description
  * category
  * city
  * address
  * owner_company
  * opening_date
  * difficulty
  * min_players
  * max_players

* Team (team of players)
  * name
  * players list

* Reservation (for a game)
  * room
  * team
  * start_time

* Game (played)
  * room
  * team
  * game_date
  * duration
  * used_jokers_count

* Review
  * player
  * room
  * date
  * content
  * decors_rate
  * puzzle_rate
  * staff_rate
  * story_rate
  * total_rate

## API Endpoints

#### **/api/v1/accounts/register/**
*	post

*Create a new user. No authentication required.*

#### **/api/v1/accounts/profile/**
*	get, put, patch, delete

*Update current user details. Authentication is required.*

#### **/api/v1/organizations/companies/**
*	get

*Returns a list of all companies. No authentication required. 
Optional filtering, searching, ordering and pagination.*

#### **/api/v1/organizations/company/**
*	post

*Create a company. Allowed for superuser only.*

#### **/api/v1/organizations/company/:id/**
*	get, put, patch, delete

*Read, update or delete a company. Allowed for superuser only.*

#### **/api/v1/organizations/employees/**
*	get
 
*Returns a list of all employees. Allowed for superuser only.
Optional filtering, ordering and pagination.*

#### **/api/v1/organizations/employee/**
*	post

*Create an employee. Allowed for superuser only.*

#### **/api/v1/organizations/employee/:id/**
*	get, put, patch, delete

*Read, update or delete an employee. Allowed for superuser only.*

#### **/api/v1/escape/rooms/**
*	get

*Returns a list of all escape rooms. No authentication required.
Optional filtering, searching, ordering and pagination.*

#### **/api/v1/escape/room/**
*	post

*Create an escape room. Allowed for an employee of escape room's company and superuser only.*

#### **/api/v1/escape/room/:id/**
*	get, put, patch, delete

*Read, update or delete an escape room. Allowed for an employee of escape room's company and superuser only.*

#### **/api/v1/escape/teams/**
*	get

*Returns a list of all teams. No authentication required.
Optional filtering, searching, ordering and pagination.*

#### **/api/v1/escape/team/**
*	post

*Create a team. Allowed for a member of the created team and superuser only.*

#### **/api/v1/escape/team/:id/**
*	get, put, patch, delete

*Read, update or delete a team. Allowed for a team member and superuser only.*

#### **/api/v1/escape/reservations/**
*	get

*Returns a list of all reservations made. No authentication required.
Optional filtering, ordering and pagination.*

#### **/api/v1/escape/reservation/**
*	post

*Create a game reservation. Allowed for a team member, an employee of escape room's company or superuser.*

#### **/api/v1/escape/reservation/:id/**
*	get, put, patch, delete

*Read, update or delete a game reservation. Allowed for a team member, an employee of escape room's company or superuser.*

#### **/api/v1/escape/games/**
*	get

*Returns a list of all records for games played. No authentication required.
Optional filtering, ordering and pagination.*

#### **/api/v1/escape/game/**
*	post

*Create a record for a game played. Allowed for an employee of escape room's company and superuser only.*

#### **/api/v1/escape/game/:id/**
*	get, put, patch, delete

*Read, update or delete a record for a game played. Allowed for an employee of escape room's company and superuser only.*

#### **/api/v1/escape/reviews/**
*	get

*Returns a list of all reviews written. No authentication required.
Optional filtering, searching, ordering and pagination.*

#### **/api/v1/escape/review/**
*	post

*Create a review. Allowed for authenticated user only.*

#### **/api/v1/escape/review/:id/**
*	get, put, patch, delete

*Read, update or delete a review written. Allowed for the review writer and superuser only.*

